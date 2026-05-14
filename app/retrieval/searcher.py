# File    : app/retrieval/searcher.py
# Purpose : Load FAISS index and retrieve top-k chunks for a query

import faiss
import numpy as np
import json
from sentence_transformers import SentenceTransformer
from config import EMBEDDING_MODEL, FAISS_INDEX_PATH, METADATA_PATH, TOP_K

model    = SentenceTransformer(EMBEDDING_MODEL)
index    = faiss.read_index(FAISS_INDEX_PATH)

with open(METADATA_PATH, "r") as f:
    metadata = json.load(f)


def search(query: str, top_k: int = TOP_K) -> list[dict]:
    vector = model.encode(query, normalize_embeddings=True)
    vector = np.array([vector], dtype="float32")

    scores, indices = index.search(vector, top_k)

    results = []
    for score, idx in zip(scores[0], indices[0]):
        if idx == -1:
            continue
        entry = metadata[idx].copy()
        entry["score"] = round(float(score), 4)
        results.append(entry)

    return results