# File    : app/ingestion/chunker.py
# Purpose : Split extracted pages into overlapping text chunks

from config import CHUNK_SIZE, CHUNK_OVERLAP


def chunk_page(page: dict) -> list[dict]:
    text     = page["text"]
    chunks   = []
    start    = 0
    idx      = 0

    while start < len(text):
        end   = start + CHUNK_SIZE
        chunk = text[start:end].strip()

        if chunk:
            chunks.append({
                "chunk_id" : f"{page['doc_title']}_p{page['page']}_c{idx}",
                "text"     : chunk,
                "page"     : page["page"],
                "source"   : page["source"],
                "doc_title": page["doc_title"]
            })
            idx += 1

        start += CHUNK_SIZE - CHUNK_OVERLAP

    return chunks


def chunk_all_pages(pages: list[dict]) -> list[dict]:
    all_chunks = []
    for page in pages:
        all_chunks.extend(chunk_page(page))
    print(f"Total chunks: {len(all_chunks)}")
    return all_chunks