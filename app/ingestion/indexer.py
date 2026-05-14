# File    : app/ingestion/indexer.py
# Purpose : Build and save FAISS index from embedded chunks

import faiss
import numpy as np
import json
import os
from config import EMBEDDING_DIMS, FAISS_INDEX_PATH, METADATA_PATH


def build_index(embedded_chunks: list[dict]) -> None:
    os.makedirs(os.path.dirname(FAISS_INDEX_PATH), exist_ok=True)

    vectors  = np.array([chunk["values"] for chunk in embedded_chunks], dtype="float32")
    metadata = [chunk["metadata"] for chunk in embedded_chunks]

    index = faiss.IndexFlatIP(EMBEDDING_DIMS)
    faiss.normalize_L2(vectors)
    index.add(vectors)

    faiss.write_index(index, FAISS_INDEX_PATH)

    with open(METADATA_PATH, "w") as f:
        json.dump(metadata, f)

    print(f"Index built   : {index.ntotal} vectors")
    print(f"Saved index   : {FAISS_INDEX_PATH}")
    print(f"Saved metadata: {METADATA_PATH}")