
import unittest

from app.retrieval import search_chunks, tokenize


class TestRetrieval(unittest.TestCase):
    def test_tokenize_is_case_insensitive(self):
        self.assertEqual(
            tokenize("Python PYTHON"),
            {"python"},
        )

    def test_returns_most_relevant_chunk_first(self):
        chunks = [
            "The weather is sunny today.",
            "Machine learning trains models using data.",
            "Machine learning models learn patterns from data.",
        ]

        result = search_chunks(
            "machine learning models",
            chunks,
            top_k=2,
        )

        self.assertEqual(result, [chunks[1], chunks[2]])

    def test_no_matching_words_returns_empty_list(self):
        self.assertEqual(
            search_chunks("quantum physics", ["Python programming"]),
            [],
        )

    def test_invalid_top_k(self):
        with self.assertRaises(ValueError):
            search_chunks("Python", ["Python is useful"], top_k=0)


if __name__ == "__main__":
    unittest.main()
