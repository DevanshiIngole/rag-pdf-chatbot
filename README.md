# 🤖 RAG PDF Chatbot

A **Retrieval-Augmented Generation (RAG) based conversational PDF chatbot** that allows users to upload PDF documents and ask questions about their content using Google's Gemini LLM.

The application uses **LangChain** for the RAG pipeline, **FAISS** for semantic vector search, and **Streamlit** for the interactive user interface.

## 🚀 Live Demo

> Coming soon — the application will be deployed using Streamlit Community Cloud.

## 📌 Project Overview

Traditional Large Language Models can generate incorrect or hallucinated answers when they don't have access to the information contained in a user's private documents.

This project solves that problem using a **Retrieval-Augmented Generation (RAG)** architecture.

The application:

1. Accepts PDF documents from the user.
2. Extracts text from the documents.
3. Splits the text into smaller chunks.
4. Generates vector embeddings for the chunks.
5. Stores the embeddings in a FAISS vector database.
6. Retrieves the most relevant document chunks for a user's question.
7. Sends the retrieved context to the Gemini LLM.
8. Generates an answer based on the retrieved document context.
9. Maintains conversation history for multi-turn interactions.

## 🏗️ Architecture

```text
                    ┌──────────────────┐
                    │    PDF Upload    │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  Text Extraction │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Text Chunking    │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │    Embeddings    │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ FAISS Vector DB  │
                    └────────┬─────────┘
                             │
                    User Question
                             │
                             ▼
                    ┌──────────────────┐
                    │ Semantic Search  │
                    │    Retriever     │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Retrieved Context│
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  Gemini LLM      │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Generated Answer │
                    └──────────────────┘
```

## 🛠️ Tech Stack

| Technology               | Purpose                            |
| ------------------------ | ---------------------------------- |
| Python                   | Core programming language          |
| LangChain                | RAG pipeline and LLM orchestration |
| Gemini API               | Large Language Model               |
| FAISS                    | Vector database / semantic search  |
| Streamlit                | Web interface                      |
| PyPDF                    | PDF text extraction                |
| HuggingFace / Embeddings | Document embeddings                |

## ✨ Features

* 📄 Upload and process PDF documents
* 🔎 Semantic document search
* 🧠 Retrieval-Augmented Generation
* 🤖 Gemini-powered question answering
* 💬 Multi-turn conversational interaction
* 🗂️ FAISS vector database
* 📚 Context-aware answers
* ⚡ Interactive Streamlit interface
* 🔐 API key entered securely through the application
* 🚫 Reduces hallucinations by grounding answers in retrieved document context

## 📂 Project Structure

```text
rag-pdf-chatbot/
│
├── app.py                  # Main Streamlit application
│
├── faiss_index/
│   ├── index.faiss        # FAISS vector index
│   └── index.pkl          # Stored document metadata
│
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .gitignore              # Ignored files and secrets
│
└── myenv/                  # Local virtual environment
                            # Not uploaded to GitHub
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/DevanshiIngole/rag-pdf-chatbot.git
```

### 2. Navigate to the project

```bash
cd rag-pdf-chatbot
```

### 3. Create a virtual environment

Windows:

```bash
python -m venv myenv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
.\myenv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Gemini API Key

This project requires a **Google Gemini API key**.

When you run the application, enter your API key through the Streamlit interface.

**Never commit your API key to GitHub.**

## ▶️ Run the Application

Start Streamlit using:

```bash
python -m streamlit run app.py
```

The application will be available locally at:

```text
http://localhost:8501
```

## 💡 Example Use Cases

This chatbot can be used for:

* 📖 Research papers
* 📑 Academic notes
* 📚 Books and study material
* 🏢 Company documentation
* 📋 Technical documentation
* 📄 Project reports
* 📊 Business documents

## 🔄 RAG Pipeline

The application follows this pipeline:

```text
PDF
 ↓
Text Extraction
 ↓
Text Splitting
 ↓
Embedding Generation
 ↓
FAISS Vector Store
 ↓
Similarity Search
 ↓
Relevant Context
 ↓
Gemini LLM
 ↓
Grounded Answer
```

## 🧠 Why RAG?

A standard LLM may not know the contents of a private PDF.

With RAG, the application first retrieves relevant information from the uploaded document and then provides that information to the LLM as context.

This helps produce answers that are:

* More relevant
* More context-aware
* Better grounded in the source documents
* Less prone to hallucination

## 📊 Evaluation

The project can be evaluated using **RAGAS** metrics such as:

* **Faithfulness** — measures whether the generated answer is supported by the retrieved context.
* **Answer Relevancy** — measures how relevant the generated answer is to the user's question.

Future improvements include adding automated RAGAS evaluation and comparing the RAG system against a base LLM without document retrieval.

## 🔮 Future Improvements

* [ ] Add RAGAS evaluation dashboard
* [ ] Add answer citations with page numbers
* [ ] Support multiple document formats
* [ ] Add persistent vector databases
* [ ] Add user authentication
* [ ] Improve conversational memory
* [ ] Deploy using Streamlit Community Cloud
* [ ] Add FastAPI backend
* [ ] Add automated evaluation pipeline
* [ ] Add document-level source attribution

## 👩‍💻 Author

**Devanshi Ingole**

GitHub:
https://github.com/DevanshiIngole

---

⭐ If you find this project useful, consider giving the repository a star!
