
import tempfile
import unittest
from pathlib import Path

from app.document_loader import load_text_file


class TestLoadTextFile(unittest.TestCase):
    def test_load_utf8_text_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "sample.txt"
            file_path.write_text(
                "Ciao, intelligenza artificiale!",
                encoding="utf-8",
            )

            result = load_text_file(str(file_path))

            self.assertEqual(
                result,
                "Ciao, intelligenza artificiale!",
            )


if __name__ == "__main__":
    unittest.main()
