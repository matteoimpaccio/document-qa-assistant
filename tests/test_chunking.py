
import unittest

from app.chunking import split_into_chunks


class TestSplitIntoChunks(unittest.TestCase):
    def test_empty_text(self):
        self.assertEqual(split_into_chunks(""), [])

    def test_splits_text_into_chunks(self):
        result = split_into_chunks(
            "uno due tre quattro cinque",
            chunk_size=10,
        )

        self.assertEqual(result, ["uno due", "tre", "quattro", "cinque"])

    def test_invalid_chunk_size(self):
        with self.assertRaises(ValueError):
            split_into_chunks("testo", chunk_size=0)


if __name__ == "__main__":
    unittest.main()
