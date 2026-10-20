
import unittest

from app.text_utils import normalize_text


class TestNormalizeText(unittest.TestCase):
    def test_normalize_whitespace(self):
        text = "  Artificial   Intelligence\n is useful.  "

        result = normalize_text(text)

        self.assertEqual(result, "Artificial Intelligence is useful.")


if __name__ == "__main__":
    unittest.main()
