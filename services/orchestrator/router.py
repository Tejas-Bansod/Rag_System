from fastapi import FastAPI, HTTPException
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'chains'))
from rag_chain import answer_from_docs

app = FastAPI(title="RAG API", description="One Piece RAG System")

@app.get("/")
def root():
    return {"message": "One Piece RAG API is running!"}

@app.get("/query")
def handle_query(query: str):
    if not query or query.strip() == "":
        raise HTTPException(status_code=400, detail="Query parameter is required and cannot be empty")
    
    try:
        answer = answer_from_docs(query)
        return {"query": query, "answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")
