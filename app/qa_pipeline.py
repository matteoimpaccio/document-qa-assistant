
from app.chunking import split_into_chunks
from app.document_loader import load_document
from app.retrieval import search_chunks
from app.text_utils import normalize_text


def retrieve_relevant_chunks(
    file_path: str,
    question: str,
    chunk_size: int = 500,
    top_k: int = 3,
) -> list[str]:
    """Load a document and retrieve the chunks relevant to a question."""
    text = load_document(file_path)
    normalized_text = normalize_text(text)
    chunks = split_into_chunks(normalized_text, chunk_size=chunk_size)

    return search_chunks(question, chunks, top_k=top_k)
