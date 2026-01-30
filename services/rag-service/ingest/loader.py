from langchain_community.document_loaders import TextLoader
from pathlib import Path

# project root nikalna
BASE_DIR = Path(__file__).resolve().parents[3]

def load_documents():
    txt_path = BASE_DIR / "data" / "raw" / "one_piece.txt"

    if not txt_path.exists():
        raise FileNotFoundError(f"File not found: {txt_path}")

    loader = TextLoader(
        file_path=str(txt_path),
        encoding="utf-8"
    )

    documents = loader.load()
    return documents

