# Document Q&A Assistant

A Python-based document question-answering project that retrieves relevant passages from PDF and TXT documents.

This project is being developed as a practical introduction to AI engineering, document processing, information retrieval, and LLM application architecture.

## Current Features

- Load text from `.txt` files.
- Extract text from `.pdf` files.
- Normalize whitespace in extracted text.
- Split document text into configurable chunks.
- Retrieve relevant chunks using keyword overlap.
- Validate core functionality with automated unit tests.

## How It Works

1. Load a PDF or TXT document.
2. Normalize the extracted text.
3. Split the text into smaller chunks.
4. Compare the user's question with the chunks.
5. Return the most relevant passages.

## Tech Stack

- Python 3.13
- pypdf
- unittest
- Git and GitHub

## Project Status

**Early development.**

The current retrieval system uses keyword overlap. LLM-based answer generation, semantic search, and evaluation are planned future improvements.

## Running Locally

Clone the repository:

```bash
git clone https://github.com/matteoimpaccio/document-qa-assistant.git
cd document-qa-assistant
```

Create and activate a virtual environment on macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the test suite:

```bash
python -m unittest discover -s tests -v
```

## Planned Improvements

- Add a command-line interface for asking questions about documents.
- Improve retrieval beyond keyword matching.
- Integrate an LLM to generate answers grounded in retrieved passages.
- Add retrieval and answer-quality evaluation.
- Explore an API using FastAPI.
- Add deployment and monitoring.

## Author

**Matteo Impaccio**

Computer Science student building practical AI engineering projects.

- GitHub: https://github.com/matteoimpaccio
