# File    : app/api/routes.py
# Purpose : FastAPI routes for query and response generation

from fastapi import APIRouter
from pydantic import BaseModel
from groq import Groq
from app.retrieval.searcher import search
from config import GROQ_API_KEY, LLM_MODEL

client = Groq(api_key=GROQ_API_KEY)
router = APIRouter()


class QueryRequest(BaseModel):
    question: str


class QueryResponse(BaseModel):
    answer  : str
    sources : list[dict]


def build_prompt(question: str, chunks: list[dict]) -> str:
    context = ""
    for i, chunk in enumerate(chunks):
        context += f"\n[{i+1}] Source: {chunk['doc_title']} | Page: {chunk['page']}\n{chunk['text']}\n"

    return f"""You are a clinical guidelines assistant. Answer the question strictly based on the provided context.
If the answer is not in the context, say "This information is not available in the current guidelines."
Do not make up any medical information.

Context:
{context}

Question: {question}

Answer:"""


@router.post("/query", response_model=QueryResponse)
def query(request: QueryRequest):
    chunks   = search(request.question)
    prompt   = build_prompt(request.question, chunks)

    response = client.chat.completions.create(
        model    = LLM_MODEL,
        messages = [{"role": "user", "content": prompt}]
    )

    answer  = response.choices[0].message.content
    sources = [{"doc_title": c["doc_title"], "page": c["page"], "score": c["score"]} for c in chunks]

    return QueryResponse(answer=answer, sources=sources)