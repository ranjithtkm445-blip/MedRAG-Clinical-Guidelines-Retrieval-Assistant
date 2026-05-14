# File    : config.py
# Purpose : Load environment variables and central config

from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY         = os.getenv("GROQ_API_KEY")

PDF_DIR              = "pdf"
CHUNK_SIZE           = 500
CHUNK_OVERLAP        = 50
EMBEDDING_MODEL      = "BAAI/bge-base-en-v1.5"
EMBEDDING_DIMS       = 768
TOP_K                = 5
LLM_MODEL            = "llama-3.1-8b-instant"
FAISS_INDEX_PATH     = "data/vectorstore/faiss.index"
METADATA_PATH        = "data/vectorstore/metadata.json"