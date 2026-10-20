
from pathlib import Path

from pypdf import PdfReader


def load_text_file(file_path: str) -> str:
    """Load text content from a UTF-8 encoded file."""
    path = Path(file_path)
    return path.read_text(encoding="utf-8")




def load_pdf_file(file_path: str) -> str:
    """Extract text from a PDF file."""
    reader = PdfReader(file_path)

    pages = []
    for page in reader.pages:
        text = page.extract_text() or ""
        pages.append(text)

    return "\n".join(pages)


def load_document(file_path: str) -> str:
    """Load a supported document based on its file extension."""
    path = Path(file_path)
    suffix = path.suffix.lower()

    if suffix == ".txt":
        return load_text_file(str(path))

    if suffix == ".pdf":
        return load_pdf_file(str(path))

    raise ValueError(
        f"Unsupported file type: {suffix or 'no extension'}"
    )

