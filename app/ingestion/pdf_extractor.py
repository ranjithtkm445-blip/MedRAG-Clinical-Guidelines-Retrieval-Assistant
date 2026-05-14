# File    : app/ingestion/pdf_extractor.py
# Purpose : Extract text and metadata from PDF files using PyMuPDF

import fitz
import os
from config import PDF_DIR


def extract_pages(pdf_path: str) -> list[dict]:
    doc = fitz.open(pdf_path)
    pages = []
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text().strip()
        if text:
            pages.append({
                "text"     : text,
                "page"     : page_num + 1,
                "source"   : os.path.basename(pdf_path),
                "doc_title": os.path.splitext(os.path.basename(pdf_path))[0]
            })
    doc.close()
    return pages


def extract_all_pdfs() -> list[dict]:
    all_pages = []
    for filename in os.listdir(PDF_DIR):
        if filename.endswith(".pdf"):
            full_path = os.path.join(PDF_DIR, filename)
            print(f"Extracting: {filename}")
            pages = extract_pages(full_path)
            print(f"  -> {len(pages)} pages extracted")
            all_pages.extend(pages)
    return all_pages