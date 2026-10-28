
def split_into_chunks(text: str, chunk_size: int = 500) -> list[str]:
    """Split text into chunks of approximately chunk_size characters."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero")

    words = text.split()
    chunks = []
    current_chunk = []
    current_length = 0

    for word in words:
        additional_length = len(word) if not current_chunk else len(word) + 1

        if current_chunk and current_length + additional_length > chunk_size:
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]
            current_length = len(word)
        else:
            current_chunk.append(word)
            current_length += additional_length

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks
