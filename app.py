import streamlit as st
from PyPDF2 import PdfReader

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.documents import Document

from datetime import datetime
import pandas as pd
import base64


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Chat with Multiple PDFs",
    page_icon="📚",
    layout="wide"
)


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "pdf_names" not in st.session_state:
    st.session_state.pdf_names = []


# --------------------------------------------------
# PDF TEXT EXTRACTION
# --------------------------------------------------

def get_pdf_text(pdf_docs):

    text = ""

    for pdf in pdf_docs:

        reader = PdfReader(pdf)

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


# --------------------------------------------------
# TEXT CHUNKING
# --------------------------------------------------

def get_text_chunks(text):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150
    )

    return text_splitter.split_text(text)


# --------------------------------------------------
# CREATE VECTOR STORE
# --------------------------------------------------

def create_vector_store(text_chunks):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = FAISS.from_texts(
        text_chunks,
        embedding=embeddings
    )

    return vector_store


# --------------------------------------------------
# GEMINI
# --------------------------------------------------

def get_llm(api_key):

    return ChatGoogleGenerativeAI(
        model="gemini-3.5-flash-lite",
        google_api_key=api_key
    )


# --------------------------------------------------
# ASK QUESTION
# --------------------------------------------------

def ask_question(question, api_key):

    vector_store = st.session_state.vector_store

    if vector_store is None:

        st.warning(
            "Please upload and process your PDF files first."
        )

        return

    # Search PDF for relevant chunks
    docs = vector_store.similarity_search(
        question,
        k=4
    )

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    prompt_template = """
You are a helpful PDF question-answering assistant.

Answer the user's question using ONLY the information
contained in the provided context.

If the answer cannot be found in the context,
say:

"Answer is not available in the provided PDF."

Do not make up information.

Context:
{context}

Question:
{question}

Answer:
"""

    prompt = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question"]
    )

    final_prompt = prompt.format(
        context=context,
        question=question
    )

    try:

        llm = get_llm(api_key)

        with st.spinner("Thinking..."):

            response = llm.invoke(final_prompt)

        answer = response.content

        # Save conversation
        st.session_state.conversation_history.append(
            (
                question,
                answer,
                "Google AI",
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
                ", ".join(st.session_state.pdf_names)
            )
        )

        return answer

    except Exception as e:

        error_text = str(e)

        if "429" in error_text or "RESOURCE_EXHAUSTED" in error_text:

            st.error(
                "Gemini API quota has been exceeded. "
                "Please check your Google AI Studio quota/billing "
                "or wait until your quota resets."
            )

        else:

            st.error(
                f"Gemini API error:\n\n{error_text}"
            )

        return None


# --------------------------------------------------
# DOWNLOAD CONVERSATION
# --------------------------------------------------

def download_history():

    if len(st.session_state.conversation_history) == 0:

        return

    df = pd.DataFrame(
        st.session_state.conversation_history,
        columns=[
            "Question",
            "Answer",
            "Model",
            "Timestamp",
            "PDF Name"
        ]
    )

    csv = df.to_csv(index=False)

    b64 = base64.b64encode(
        csv.encode()
    ).decode()

    href = (
        f'<a href="data:file/csv;base64,{b64}" '
        f'download="conversation_history.csv">'
        f'📥 Download Conversation History'
        f'</a>'
    )

    st.sidebar.markdown(
        href,
        unsafe_allow_html=True
    )


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("📚 PDF Chatbot")

api_key = st.sidebar.text_input(
    "Enter your Google API Key:",
    type="password"
)

st.sidebar.markdown(
    "Get your API key from "
    "[Google AI Studio](https://aistudio.google.com/)"
)


# --------------------------------------------------
# PDF UPLOAD
# --------------------------------------------------

pdf_docs = st.sidebar.file_uploader(
    "Upload your PDF files",
    type=["pdf"],
    accept_multiple_files=True
)


# --------------------------------------------------
# PROCESS PDF
# --------------------------------------------------

if st.sidebar.button(
    "Submit & Process",
    type="primary"
):

    if not pdf_docs:

        st.sidebar.warning(
            "Please upload at least one PDF."
        )

    else:

        with st.spinner(
            "Reading PDFs and creating vector database..."
        ):

            # Read PDFs
            raw_text = get_pdf_text(pdf_docs)

            if not raw_text.strip():

                st.error(
                    "No readable text was found in the PDF."
                )

            else:

                # Split text
                text_chunks = get_text_chunks(
                    raw_text
                )

                # Create FAISS
                vector_store = create_vector_store(
                    text_chunks
                )

                # Store in session
                st.session_state.vector_store = (
                    vector_store
                )

                st.session_state.pdf_names = [
                    pdf.name for pdf in pdf_docs
                ]

                st.sidebar.success(
                    f"Processed {len(text_chunks)} chunks."
                )


# --------------------------------------------------
# RESET
# --------------------------------------------------

if st.sidebar.button("Reset"):

    st.session_state.vector_store = None

    st.session_state.conversation_history = []

    st.session_state.pdf_names = []

    st.rerun()


# --------------------------------------------------
# MAIN UI
# --------------------------------------------------

st.title(
    "Chat with Multiple PDFs 📚"
)

st.write(
    "Upload your PDF files, process them, "
    "and ask questions about their contents."
)


# --------------------------------------------------
# QUESTION
# --------------------------------------------------

question = st.text_input(
    "Ask a Question from the PDF Files"
)


if question:

    if not api_key:

        st.warning(
            "Please enter your Google API key."
        )

    elif st.session_state.vector_store is None:

        st.warning(
            "Please upload and process your PDF files first."
        )

    else:

        answer = ask_question(
            question,
            api_key
        )

        if answer:

            st.markdown("### 🤖 Answer")

            st.write(answer)


# --------------------------------------------------
# CONVERSATION HISTORY
# --------------------------------------------------

if st.session_state.conversation_history:

    st.markdown("---")

    st.subheader("Conversation History")

    for question, answer, model, timestamp, pdf_name in reversed(
        st.session_state.conversation_history
    ):

        st.markdown(
            f"**You:** {question}"
        )

        st.markdown(
            f"**AI:** {answer}"
        )

        st.caption(
            f"{timestamp} | {pdf_name}"
        )

        st.markdown("---")

    download_history()