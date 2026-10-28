
import re


def tokenize(text: str) -> set[str]:
    """Convert text into a set of lowercase words."""
    return set(re.findall(r"\b\w+\b", text.lower()))


def search_chunks(
    question: str,
    chunks: list[str],
    top_k: int = 3,
) -> list[str]:
    """Return the chunks with the most word overlap with the question."""
    if top_k <= 0:
        raise ValueError("top_k must be greater than zero")

    question_words = tokenize(question)

    if not question_words:
        return []

    scored_chunks = []

    for index, chunk in enumerate(chunks):
        chunk_words = tokenize(chunk)
        score = len(question_words & chunk_words)

        if score > 0:
            scored_chunks.append((score, index, chunk))

    scored_chunks.sort(key=lambda item: (-item[0], item[1]))

    return [chunk for _, _, chunk in scored_chunks[:top_k]]
