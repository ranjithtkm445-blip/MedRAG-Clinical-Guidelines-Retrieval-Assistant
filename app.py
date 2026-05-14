# File    : app.py
# Purpose : Streamlit frontend for MedRAG Clinical Guidelines Assistant

import streamlit as st
from app.retrieval.searcher import search
from groq import Groq
from config import GROQ_API_KEY, LLM_MODEL

client = Groq(api_key=GROQ_API_KEY)

st.set_page_config(
    page_title = "MedRAG Clinical Assistant",
    page_icon  = "🏥",
    layout     = "wide"
)

st.title("MedRAG Clinical Guidelines Assistant")
st.caption("Answers grounded in WHO clinical guidelines — Dengue & Hypertension")
st.divider()

query = st.text_input("Enter your clinical question:", placeholder="e.g. What are the symptoms of dengue fever?")

if st.button("Search") and query:
    with st.spinner("Retrieving from guidelines..."):
        chunks = search(query)

        context = ""
        for i, chunk in enumerate(chunks):
            context += f"\n[{i+1}] Source: {chunk['doc_title']} | Page: {chunk['page']}\n{chunk['text']}\n"

        prompt = f"""You are a clinical guidelines assistant. Answer the question strictly based on the provided context.
If the answer is not in the context, say "This information is not available in the current guidelines."
Do not make up any medical information.

Context:
{context}

Question: {query}

Answer:"""

        response = client.chat.completions.create(
            model    = LLM_MODEL,
            messages = [{"role": "user", "content": prompt}]
        )

        answer = response.choices[0].message.content

    st.subheader("Answer")
    st.write(answer)

    st.divider()
    st.subheader("Sources")
    for chunk in chunks:
        with st.expander(f"{chunk['doc_title'].upper()} — Page {chunk['page']} (score: {chunk['score']})"):
            st.write(chunk["text"])