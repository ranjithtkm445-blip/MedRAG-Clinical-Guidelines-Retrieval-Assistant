# File    : ingest.py
# Purpose : Run full ingestion pipeline — extract, chunk, embed, index

from app.ingestion.pdf_extractor import extract_all_pdfs
from app.ingestion.chunker import chunk_all_pages
from app.ingestion.embedder import embed_chunks
from app.ingestion.indexer import build_index

if __name__ == "__main__":
    print("=== Step 1: Extracting PDFs ===")
    pages = extract_all_pdfs()

    print("\n=== Step 2: Chunking ===")
    chunks = chunk_all_pages(pages)

    print("\n=== Step 3: Embedding ===")
    embedded = embed_chunks(chunks)

    print("\n=== Step 4: Building FAISS Index ===")
    build_index(embedded)

    print("\n=== Ingestion Complete ===")