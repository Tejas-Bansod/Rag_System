# Import necessary functions and modules
from loader import load_documents
from chunker import chunk_docs
from embedder import embed_documents

# Load the documents
docs = load_documents()

# Alternatively, load documents from Wikipedia
# docs = load_wikipedia("Artificial Intelligence")

# Split the documents into chunks
chunks = chunk_docs(docs)

# Embed the chunks using OpenAI embeddings
embed_documents(chunks)

# Print a success message
print("✅ Documents indexed")
