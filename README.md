# 📄 Document Q&A Assistant (RAG) - V2

An AI-powered document question-answering system that allows users to upload a PDF and ask questions. The application uses **Retrieval Augmented Generation (RAG)** to retrieve relevant information from documents and generate accurate answers using Google's Gemini LLM.

---

## 🚀 Project Overview

Traditional document search requires manually reading through hundreds of pages.

This project solves that problem by creating an AI assistant that can:

- Understand uploaded documents
- Search relevant information using semantic similarity
- Generate answers from document context
- Provide source references

The system follows a complete RAG pipeline:
PDF Document
|
↓
Text Extraction
|
↓
Text Chunking
|
↓
Embeddings Generation
|
↓
Chroma Vector Database
|
↓
Semantic Retrieval
|
↓
Gemini LLM
|
↓
AI Generated Answer

---

# ✨ Features

## 📄 PDF Processing

- Upload PDF documents
- Extract text from documents
- Split large documents into meaningful chunks

## 🔍 Semantic Search

- Converts document chunks into embeddings
- Stores embeddings in Chroma Vector Database
- Retrieves the most relevant information for user questions

## 🤖 AI Answer Generation

- Uses Google Gemini LLM
- Answers questions using only retrieved document context
- Reduces hallucination by grounding answers in source documents

## 📚 Source References

The system provides document references for retrieved information.

Example:
Answer:
Employees are entitled to 30 days annual leave after one year.

Sources:
📄 UAE_labour_law.pdf
Page 20

---

# 🛠️ Tech Stack

## Programming Language

- Python 3.11

## AI / ML

- Google Gemini API
- LangChain
- Sentence Transformers

## Vector Database

- ChromaDB

## Document Processing

- PyPDF

## Frontend

- Streamlit

---

# 📂 Project Structure
document-qa-assistant/

│
├── streamlit_app.py # Streamlit user interface
│
├── index_documents.py # PDF processing and vector creation
│
├── embeddings.py # Embedding model configuration
│
├── retriever.py # Semantic search logic
│
├── llm.py # Gemini LLM integration
│
├── documents/
│ └── sample.pdf
│
├── vector_db/ # Chroma vector database
│
├── requirements.txt
│
├── README.md
│
└── .gitignore



---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone <repository-url>

cd document-qa-assistant
2. Create Virtual Environment
python3.11 -m venv .venv

Activate:

Mac/Linux
source .venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
🔑 Environment Setup

Create a .env file:

GOOGLE_API_KEY=your_gemini_api_key
📚 Create Vector Database

Add your PDF inside:

documents/

Run:

python index_documents.py

This creates:

vector_db/

containing document embeddings.

▶️ Run Application

Start Streamlit:

streamlit run streamlit_app.py

The application will open in your browser.

💡 Example Questions

Using UAE Labour Law PDF:

How many annual leave days are employees entitled to?
What is Article 75 about?
What are the employee rights mentioned in the document?
🧠 How RAG Works in This Project

Instead of sending the entire PDF to an AI model:

User asks a question
The system converts the question into an embedding
Chroma searches for similar document chunks
Relevant context is sent to Gemini
Gemini generates an answer based only on that context
🔮 Future Improvements (V3)

The next version will introduce LangGraph Agentic RAG.

Planned improvements:

AI workflow orchestration using LangGraph
Query rewriting
Retrieval validation
Decision-based AI agents
Better reasoning pipeline
Conversation memory

Architecture:

User Question
      |
      ↓
LangGraph Workflow
      |
      ↓
Retrieve Documents
      |
      ↓
Evaluate Context
      |
      ↓
Generate Answer
👩‍💻 Author

Shaik Afreen

AI Engineer | Full Stack Developer

Building intelligent systems using Generative AI, RAG, and Agentic AI.
