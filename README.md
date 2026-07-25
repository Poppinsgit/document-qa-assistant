# Document Q&A Assistant (RAG)

An AI-powered document question-answering system built using **Retrieval-Augmented Generation (RAG)**. Upload a PDF, ask questions in plain English, and get answers grounded in the document's actual content — with page-level source citations, so every answer can be traced back to where it came from.

This project evolved across three versions, each adding real architectural depth:

```
V1: Linear RAG pipeline (CLI)
        ↓
V2: + Streamlit UI, live upload, source citations
        ↓
V3: + LangGraph agentic workflow (retrieve → generate as graph nodes)
```

---

## How It Works (V3 Architecture)

```
User Question
      ↓
LangGraph Workflow
      ↓
retrieve_node → semantic search (ChromaDB) → relevant chunks
      ↓
generate_node → Gemini LLM → grounded answer
      ↓
Answer + Source Citations (filename + page number)
```

The retrieval and generation steps are implemented as explicit graph nodes with a shared typed state (`AgentState`), rather than a single linear script — the foundation for future extensions like query rewriting, retrieval validation, or multi-step reasoning.

---

## Version History

### V1 — Core RAG Pipeline
- PDF text extraction and chunking
- Embedding generation (Sentence Transformers)
- Vector storage and semantic search (ChromaDB)
- Answer generation grounded in retrieved context (Gemini via LangChain)
- Command-line interface

### V2 — Usable Application
- Streamlit web interface with live PDF upload and indexing
- Source citations (filename + page number) for every answer
- Cleaner, single-responsibility LLM integration

### V3 — Agentic Workflow (LangGraph)
- Migrated from a linear script to a **LangGraph state graph**: `retrieve_node` → `generate_node`, connected via typed state (`AgentState`)
- Sets up the architecture for agentic extensions — conditional routing, retrieval validation, and multi-step reasoning in future iterations
- Error-handled LLM calls (graceful failure instead of a crash if the API errors)

---

## Tech Stack

- Python 3.11
- LangChain / LangGraph
- ChromaDB (vector database)
- Sentence Transformers (embeddings)
- Google Gemini API (LLM)
- Streamlit (interface)
- PyPDF (document parsing)

---

## Project Structure

```
document-qa-assistant/
├── streamlit_app.py       # Streamlit UI, invokes the LangGraph workflow
├── graph.py                # LangGraph state graph definition
├── nodes.py                 # retrieve_node and generate_node implementations
├── state.py                 # Shared AgentState (TypedDict)
├── index_documents.py       # PDF processing, chunking, vector DB creation
├── retriever.py              # Semantic search against ChromaDB
├── embeddings.py              # Embedding model configuration
├── llm.py                      # Gemini LLM integration, with error handling
├── documents/                   # Uploaded/indexed PDFs
├── vector_db/                    # Chroma vector database (generated)
├── requirements.txt
└── README.md
```

---

## Setup

Install dependencies:
```bash
pip install -r requirements.txt
```

Create a `.env` file:
```
GOOGLE_API_KEY=your_gemini_api_key
```

Run the app:
```bash
streamlit run streamlit_app.py
```
Upload a PDF, ask a question, and the app will index the document and answer using only its content.

---

## Example

**Question:** How many annual leave days are employees entitled to?

**Answer:** According to Article 75 of UAE Labour Law, employees are entitled to 30 days annual leave after completing more than one year of service.

**Sources:** 📄 UAE_labour_law.pdf | Page 20

---

## What This Project Demonstrates

- End-to-end RAG system design: chunking, embeddings, vector search, grounded generation
- Practical experience migrating a linear pipeline to a LangGraph-based agentic workflow
- Iterative, versioned development — each release adds a genuine architectural capability, not just surface changes

## Future Improvements

- Conditional routing and retrieval validation as explicit graph nodes
- Multi-document support with cross-document citation
- Conversation memory across multiple questions
- Query rewriting for improved retrieval accuracy

---

## Author

Shaik Afreen Banu
AI/ML Engineer | Full Stack Developer
