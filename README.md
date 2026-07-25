# 📄 Document Q&A Assistant (RAG)

An AI-powered document question-answering system built using **Retrieval-Augmented Generation (RAG)**.

The application allows users to upload documents, retrieve relevant information using semantic search, and generate accurate answers using Large Language Models.

---

## 🚀 How It Works
PDF Document
|
↓
Text Extraction
|
↓
Text Chunking
|
↓
Embedding Generation
|
↓
Vector Database (Chroma)
|
↓
Semantic Search
|
↓
LLM Answer Generation

---

## 🧠 Key Concepts Implemented

### 1. Document Processing
- Extracts text from PDF documents
- Splits large documents into smaller meaningful chunks

### 2. Embeddings
- Converts text into numerical vectors
- Captures semantic meaning instead of exact keyword matching

### 3. Vector Search
- Stores embeddings in ChromaDB
- Retrieves the most relevant document sections based on user queries

### 4. Retrieval-Augmented Generation
- Provides retrieved context to the LLM
- Generates answers grounded in the uploaded documents

---

## 🛠️ Tech Stack

- Python 3.11
- LangChain
- Chroma Vector Database
- Sentence Transformers
- Google Gemini API
- PyPDF

---

## 📂 Project Structure
document-qa-assistant/

├── documents/
│ └── PDF files

├── vector_db/
│ └── Chroma embeddings

├── pdf_loader.py
├── embeddings.py
├── llm.py
├── chat.py

├── requirements.txt
├── README.md
└── .gitignore

---

## 💡 Example

Question:

> How many annual leave days are employees entitled to?

Answer:

> According to Article 75 of UAE Labour Law, employees are entitled to 30 days annual leave after completing more than one year of service.

---

## 🎯 Future Improvements

- Streamlit web interface
- Multiple document upload
- Source citations with page numbers
- Conversation memory
- LangGraph agent workflow

---

## 👩‍💻 Author

Shaik Afreen

AI Engineer | Full Stack Developer