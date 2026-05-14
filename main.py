# File    : main.py
# Purpose : FastAPI application entry point

from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="MedRAG Clinical Guidelines Assistant")
app.include_router(router)


@app.get("/")
def root():
    return {"status": "MedRAG is running"}