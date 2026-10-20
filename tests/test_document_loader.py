
import tempfile
import unittest
from pathlib import Path

from unittest.mock import MagicMock, patch

from app.document_loader import load_document, load_text_file

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

    def test_unsupported_file_type(self):
        with self.assertRaises(ValueError):
            load_document("report.docx")


    @patch("app.document_loader.PdfReader")
    def test_load_pdf_file(self, mock_pdf_reader):
        from app.document_loader import load_pdf_file

        first_page = MagicMock()
        first_page.extract_text.return_value = "First page"

        second_page = MagicMock()
        second_page.extract_text.return_value = "Second page"

        mock_pdf_reader.return_value.pages = [
            first_page,
            second_page,
        ]

        result = load_pdf_file("sample.pdf")

        self.assertEqual(result, "First page\nSecond page")


if __name__ == "__main__":
    unittest.main()
