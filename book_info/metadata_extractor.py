from typing import Optional, Tuple
from PyPDF2 import PdfFileReader

class MetadataExtractor:
    """Extracts metadata from a PDF file."""

    @staticmethod
    def extract_book_info(filepath: str) -> Tuple[Optional[str], Optional[str]]:
        """Extract metadata from a PDF file"""
        try:
            with open(filepath, 'rb') as f:
                reader = PdfFileReader(f)
                info = reader.getDocumentInfo()
                title = info.title if info.title else None
                author = info.author if info.author else None
                return title, author
        except Exception as e:
            print(f"Failed to extract metadata from {filepath}: {e}")
            return None, None
