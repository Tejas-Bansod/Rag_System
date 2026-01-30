from fastapi import APIRouter
from services.orchestrator.router import handle_query

router = APIRouter()

@router.post("/chat")
def chat(query: str):
    return handle_query(query)
