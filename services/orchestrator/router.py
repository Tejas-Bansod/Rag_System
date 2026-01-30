from fastapi import FastAPI
from services.orchestrator.chains.rag_chain import answer_from_docs

app = FastAPI()

@app.get("/query")
def handle_query(query: str):
    answer = answer_from_docs(query)
    return {"answer": answer}
