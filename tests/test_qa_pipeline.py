
import tempfile
import unittest
from pathlib import Path

from app.qa_pipeline import retrieve_relevant_chunks


class TestQAPipeline(unittest.TestCase):
    def test_retrieves_relevant_chunks_from_text_file(self):
        content = (
            "Python is a programming language. "
            "Machine learning uses data to train models. "
            "The ocean contains salt water."
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "document.txt"
            file_path.write_text(content, encoding="utf-8")

            results = retrieve_relevant_chunks(
                str(file_path),
                "machine learning models",
                chunk_size=100,
                top_k=2,
            )

        self.assertTrue(results)
        self.assertIn("Machine learning", results[0])

    def test_returns_empty_list_when_nothing_matches(self):
        content = "The ocean contains salt water."

        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "document.txt"
            file_path.write_text(content, encoding="utf-8")

            results = retrieve_relevant_chunks(
                str(file_path),
                "quantum computing",
            )

        self.assertEqual(results, [])


if __name__ == "__main__":
    unittest.main()
