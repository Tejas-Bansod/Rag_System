from langchain import RetrievalQA
from services.inference_service.model_loader import load_llm
from services.rag_service.vector_store import get_vector_store

def answer_from_docs(question):
    llm = load_llm()
    db = get_vector_store()

    qa = RetrievalQA(
        llm=llm,
        retriever=db,
        chain_type="stuff"
    )

    return qa(question)
