# File    : app/ingestion/embedder.py
# Purpose : Generate embeddings locally using sentence-transformers

from sentence_transformers import SentenceTransformer
from config import EMBEDDING_MODEL

model = SentenceTransformer(EMBEDDING_MODEL)


def embed_text(text: str) -> list[float]:
    vector = model.encode(text, normalize_embeddings=True)
    return vector.tolist()


def embed_chunks(chunks: list[dict]) -> list[dict]:
    embedded = []
    texts = [chunk["text"] for chunk in chunks]

    print(f"Encoding {len(texts)} chunks locally...")
    vectors = model.encode(texts, normalize_embeddings=True, show_progress_bar=True, batch_size=32)

    for i, chunk in enumerate(chunks):
        embedded.append({
            "chunk_id" : chunk["chunk_id"],
            "values"   : vectors[i].tolist(),
            "metadata" : {
                "text"     : chunk["text"],
                "page"     : chunk["page"],
                "source"   : chunk["source"],
                "doc_title": chunk["doc_title"]
            }
        })

    print(f"Embedding complete: {len(embedded)} chunks")
    return embedded