from langchain.chains import RetrievalQA
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'inference-service'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'rag-service'))
from model_loader import load_llm
from vector_store import get_vector_store

def answer_from_docs(question):
    llm = load_llm()
    db = get_vector_store()
    retriever = db.as_retriever()

    # Create a simple prompt template
    prompt = ChatPromptTemplate.from_template("""Answer the following question based on the provided context:

Context: {context}

Question: {input}

Answer:""")

    # Create the document chain
    document_chain = create_stuff_documents_chain(llm, prompt)
    
    # Create the retrieval chain
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    
    # Get the answer
    response = retrieval_chain.invoke({"input": question})
    return response["answer"]
