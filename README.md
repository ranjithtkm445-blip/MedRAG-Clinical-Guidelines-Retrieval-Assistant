# MedRAG — Clinical Guidelines Retrieval Assistant

MedRAG answers clinical questions from WHO guidelines using RAG, FAISS vector search, and Groq LLM — returning grounded responses with document and page citations to reduce hallucinations.

---

## Overview

MedRAG is a healthcare-focused Retrieval-Augmented Generation (RAG) platform designed to provide accurate, citation-aware answers from trusted clinical guideline documents. The system restricts responses strictly to retrieved context, attaching document title and page references with every answer.

---

## Architecture

```
Medical PDFs
      ↓
PDF Text Extraction (PyMuPDF)
      ↓
Smart Chunking Pipeline
      ↓
Embedding Generation (sentence-transformers / BAAI/bge-base-en-v1.5)
      ↓
FAISS Vector Storage (local)
      ↓
Semantic Similarity Retrieval
      ↓
Context Injection
      ↓
LLM Response Generation (Groq / LLaMA 3.1)
      ↓
Answer + Source Citations
```

---

## Features

- Clinical PDF ingestion pipeline
- Retrieval-Augmented Generation (RAG)
- Semantic medical document search
- FAISS local vector database
- Local sentence-transformers embeddings (no API cost)
- Groq LLM integration (LLaMA 3.1)
- Citation-aware responses with page references
- Hallucination reduction safeguards
- FastAPI backend
- Streamlit frontend

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, FastAPI |
| Frontend | Streamlit |
| Embeddings | sentence-transformers (BAAI/bge-base-en-v1.5) |
| Vector Store | FAISS (local) |
| LLM | Groq API (LLaMA 3.1 8B) |
| PDF Processing | PyMuPDF |

---

## Dataset

- WHO Dengue Guidelines
- WHO Hypertension Treatment Guidelines

---

## Project Structure

```
MedRAG/
├── app/
│   ├── ingestion/
│   │   ├── pdf_extractor.py
│   │   ├── chunker.py
│   │   ├── embedder.py
│   │   └── indexer.py
│   ├── retrieval/
│   │   └── searcher.py
│   └── api/
│       └── routes.py
├── data/
│   └── vectorstore/
│       ├── faiss.index
│       └── metadata.json
├── pdf/
│   ├── dengue.pdf
│   └── hypertension.pdf
├── app.py
├── main.py
├── ingest.py
├── config.py
├── requirements.txt
└── Dockerfile
```

---

## Setup

**1. Clone and install:**
```bash
git clone <repo-url>
cd MedRAG
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**2. Configure `.env`:**
```
GROQ_API_KEY=your_groq_key_here
```

**3. Run ingestion (once):**
```bash
python ingest.py
```

**4. Start Streamlit:**
```bash
streamlit run app.py
```

**5. Or start FastAPI:**
```bash
python -m uvicorn main:app --reload
```

---

## API

**POST** `/query`

```json
{
  "question": "What are the symptoms of dengue fever?"
}
```

Response:
```json
{
  "answer": "Based on the WHO guidelines...",
  "sources": [
    {"doc_title": "dengue", "page": 26, "score": 0.82}
  ]
}
```

---

## Safety

MedRAG is a clinical knowledge retrieval assistant — not a replacement for professional medical advice. The LLM is instructed to answer only from retrieved context and explicitly states when information is unavailable.

---

## Resume Line

Developed MedRAG, a healthcare-focused RAG platform using FastAPI, FAISS vector database, sentence-transformers embeddings, and Groq LLM to deliver citation-aware medical question answering from WHO clinical guideline documents.
