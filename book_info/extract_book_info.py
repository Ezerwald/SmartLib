from typing import Optional, Tuple
from .filename_extractor import FilenameExtractor
from .metadata_extractor import MetadataExtractor
from .book_info_fetcher import BookInfoFetcher
from utils import log_book_data


class BookInfoExtractor:
    def __init__(self):
        self.book_info_fetcher = BookInfoFetcher()

    def get_book_info(self, filepath: str) -> Tuple[str, str]:
        filename = filepath.split('\\')[-1]

        # Try extracting from metadata first
        title, author = self._attempt_extraction(MetadataExtractor.extract_book_info, filepath, 'Metadata')

        # If not found or incomplete, try fetching from online databases
        if not title or not author:
            query = title if title else filename
            title, author = self._attempt_extraction(self.book_info_fetcher.get_book_info_from_online_databases, query,
                                                     'Online Databases')

        # If still not found or incomplete, try extracting from filename
        if not title or not author:
            title, author = self._attempt_extraction(FilenameExtractor.extract_book_info, filename, 'Filename')

        # Finalize book info ensuring no empty values are returned
        title, author = self._finalize_book_info(title, author, filepath)

        return title, author

    def _attempt_extraction(self, extraction_method, input_data: str, method_name: str) -> Tuple[
        Optional[str], Optional[str]]:
        """
        Helper method to attempt extraction using a given method and log the results.
        """
        try:
            title, author = extraction_method(input_data)
            log_book_data(title, author)
            print(f"Extraction method '{method_name}' returned Title: {title}, Author: {author}")
            return title, author
        except Exception as e:
            print(f"Extraction method '{method_name}' failed: {e}")
            return None, None

    def _finalize_book_info(self, title: Optional[str], author: Optional[str], filepath: str) -> Tuple[str, str]:
        """
        Finalize book info ensuring no empty values are returned.
        """
        if not title:
            print('No title found')
            filename = filepath.split('\\')[-1]
            title = filename
        if not author:
            print('No author found')
            author = "No author found"
        return title, author


if __name__ == "__main__":
    extractor = BookInfoExtractor()
    filepath = "example/path/to/bookfile.pdf"
    title, author = extractor.get_book_info(filepath)
    print(f"Title: {title}, Author: {author}")
