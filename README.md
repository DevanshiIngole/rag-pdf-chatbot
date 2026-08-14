# 🤖 RAG PDF Chatbot

A **Retrieval-Augmented Generation (RAG) based conversational PDF chatbot** built with **Python, LangChain, FAISS, Google Gemini, and Streamlit**.

The application allows users to interact with PDF documents using natural language. It retrieves relevant information from the document using semantic similarity search and uses Google's Gemini LLM to generate context-aware answers.

## 🚀 Live Demo

**Try the deployed application:**

https://devanshiingole-rag-pdf-chatbot-app-sh9whb.streamlit.app/

> The application is deployed using Streamlit Community Cloud.

## 📂 GitHub Repository

https://github.com/DevanshiIngole/rag-pdf-chatbot

---

## 📌 Project Overview

Large Language Models can sometimes generate incorrect or hallucinated information when answering questions without access to relevant source documents.

This project uses **Retrieval-Augmented Generation (RAG)** to ground the LLM's responses in information retrieved from PDF documents.

The application follows this workflow:

```text
PDF Document
     │
     ▼
Text Extraction
     │
     ▼
Text Chunking
     │
     ▼
Document Embeddings
     │
     ▼
FAISS Vector Store
     │
     ▼
Semantic Retrieval
     │
     ▼
Relevant Context
     │
     ▼
Google Gemini LLM
     │
     ▼
Context-Aware Answer
```

---

## ✨ Features

* 📄 PDF document processing
* 🔎 Semantic similarity search
* 🧠 Retrieval-Augmented Generation
* 🤖 Google Gemini LLM integration
* 🗂️ FAISS vector database
* 💬 Conversational question answering
* 📚 Context-aware responses
* ⚡ Interactive Streamlit interface
* 🔐 API key entered securely through the application
* 🚫 Reduces unsupported/hallucinated responses by grounding answers in retrieved document context

---

## 🛠️ Tech Stack

| Technology        | Purpose                            |
| ----------------- | ---------------------------------- |
| **Python**        | Core programming language          |
| **LangChain**     | RAG pipeline and LLM orchestration |
| **Google Gemini** | Large Language Model               |
| **FAISS**         | Vector similarity search           |
| **Streamlit**     | Web application interface          |
| **PyPDF2**        | PDF text extraction                |
| **Pandas**        | Data processing                    |
| **python-dotenv** | Environment variable management    |

---

## 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │     PDF Upload      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   PDF Text Parser   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Text Chunking    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      Embeddings     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   FAISS Vector DB   │
                    └──────────┬──────────┘
                               │
                               │
                    ┌──────────▼──────────┐
                    │   User Question     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Semantic Retrieval  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Retrieved Context   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Gemini LLM        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Final Answer      │
                    └─────────────────────┘
```

---

## 🔄 How RAG Works in This Project

### 1. Document ingestion

The application reads the uploaded PDF and extracts its text.

### 2. Text splitting

Large documents are divided into smaller chunks so that relevant sections can be retrieved efficiently.

### 3. Embeddings

The text chunks are converted into numerical vector representations.

### 4. FAISS indexing

The embeddings are stored in a FAISS vector index for efficient similarity search.

### 5. Retrieval

When a user asks a question, the application searches the FAISS index and retrieves the most relevant document chunks.

### 6. Generation

The retrieved information is passed as context to Google's Gemini LLM.

### 7. Response

Gemini generates an answer based on the retrieved document context.

---

## 📁 Project Structure

```text
rag-pdf-chatbot/
│
├── app.py
│   └── Main Streamlit application
│
├── faiss_index/
│   ├── index.faiss
│   └── index.pkl
│
├── requirements.txt
│   └── Python dependencies
│
├── runtime.txt
│   └── Deployment/runtime configuration
│
├── README.md
│   └── Project documentation
│
└── .gitignore
    └── Files excluded from Git
```

> `myenv/` is used only for the local Python environment and is intentionally excluded from GitHub.

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/DevanshiIngole/rag-pdf-chatbot.git
```

### 2. Navigate to the project

```bash
cd rag-pdf-chatbot
```

### 3. Create a virtual environment

```bash
python -m venv myenv
```

### 4. Activate the environment

#### Windows PowerShell

```powershell
.\myenv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Gemini API Key

This application requires a **Google Gemini API key**.

The application provides an input field through the Streamlit interface where the user can provide their API key.

### Security

**Never commit an API key to GitHub.**

Do not put API keys directly inside:

```text
app.py
```

or commit files such as:

```text
.env
.streamlit/secrets.toml
```

These files are excluded through `.gitignore`.

---

## ▶️ Run Locally

After activating the virtual environment and installing dependencies:

```bash
python -m streamlit run app.py
```

The application will normally be available at:

```text
http://localhost:8501
```

---

## 🌐 Deployment

The application is deployed using **Streamlit Community Cloud**.

Deployment workflow:

```text
Local Project
      │
      ▼
    Git
      │
      ▼
   GitHub
      │
      ▼
Streamlit Community Cloud
      │
      ▼
 Public Web Application
```

### Current Deployment

**Live application:**

https://devanshiingole-rag-pdf-chatbot-app-sh9whb.streamlit.app/

---

## 🧪 Example Questions

After uploading a suitable PDF, users can ask questions such as:

```text
What is the main topic of this document?

Summarize the key findings.

What are the important conclusions?

Explain the methodology used in the document.

What are the main advantages discussed?

What are the limitations mentioned?
```

The chatbot retrieves relevant content from the document before generating the answer.

---

## 🎯 Why RAG?

A traditional LLM may not have access to the contents of a user's private document.

RAG improves this process by retrieving relevant information from the document and providing it to the LLM as context.

This helps make responses:

* More relevant
* More document-specific
* Better grounded in retrieved information
* Less dependent on the LLM's pre-trained knowledge
* Less prone to unsupported answers

---

## 📊 Evaluation

The planned evaluation methodology uses **RAGAS** metrics to evaluate the quality of the RAG pipeline.

Important metrics include:

### Faithfulness

Measures whether the generated answer is supported by the retrieved context.

### Answer Relevancy

Measures how relevant the generated answer is to the user's question.

A future version of this project can compare:

```text
Base LLM
   vs.
RAG + LLM
```

to measure the improvement in grounded responses.

---

## 🚀 Future Improvements

* [ ] Add RAGAS evaluation pipeline
* [ ] Add faithfulness and answer-relevancy scores
* [ ] Compare RAG against a base LLM
* [ ] Add source/page citations to answers
* [ ] Add support for TXT, DOCX and other document formats
* [ ] Add persistent vector database management
* [ ] Improve conversational memory
* [ ] Add FastAPI backend
* [ ] Separate frontend and backend architecture
* [ ] Add user authentication
* [ ] Add document management
* [ ] Improve UI/UX
* [ ] Add automated testing
* [ ] Add CI/CD pipeline

---

## 📈 Future Architecture

The planned production architecture is:

```text
                 ┌──────────────────┐
                 │ Streamlit Frontend│
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │  FastAPI Backend │
                 └────────┬─────────┘
                          │
              ┌───────────┴───────────┐
              │                       │
              ▼                       ▼
       ┌──────────────┐       ┌──────────────┐
       │ FAISS Vector │       │ Gemini / LLM  │
       │    Store     │       │              │
       └──────────────┘       └──────────────┘
              │                       │
              └───────────┬───────────┘
                          ▼
                  ┌───────────────┐
                  │ RAG Response  │
                  └───────────────┘
```

---

## 💼 Skills Demonstrated

This project demonstrates practical experience with:

* Python
* LangChain
* Retrieval-Augmented Generation (RAG)
* Large Language Models
* Google Gemini API
* Vector embeddings
* FAISS
* Semantic search
* Prompt engineering
* PDF processing
* Streamlit
* Git & GitHub
* Cloud deployment

---

## 👩‍💻 Author

### Devanshi Ingole

GitHub:
https://github.com/DevanshiIngole

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

**GitHub Repository:**
https://github.com/DevanshiIngole/rag-pdf-chatbot

**Live Demo:**
https://devanshiingole-rag-pdf-chatbot-app-sh9whb.streamlit.app/
