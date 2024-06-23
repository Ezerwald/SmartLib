import os
import mimetypes
from typing import List
from book_info import BookInfoExtractor
from database import DatabaseHandler


class BookProcessor:
    """
    A class to process digital books in a specified folder and add their information to a database.

    Attributes:
        folder_path (str): The path to the folder containing digital books.
        db_handler (DatabaseHandler): An instance of DatabaseHandler for managing database operations.
        book_info_extractor (BookInfoExtractor): An instance of BookInfoExtractor for extracting book information.
    """

    def __init__(self, folder_path: str, db_path: str):
        """
        Initializes the BookProcessor with the folder path and database path.

        Args:
            folder_path (str): The path to the folder containing digital books.
            db_path (str): The path to the SQLite database file.
        """
        self.folder_path = folder_path
        self.db_handler = DatabaseHandler(db_path)
        self.book_info_extractor = BookInfoExtractor()

    def process_books(self):
        """
        Processes all digital books in the specified folder and adds their information to the database.
        """
        files = self._get_all_book_files(self.folder_path)
        for filepath in files:
            self._process_book(filepath)
        self.db_handler.close_connection()

    def _get_all_book_files(self, folder_path: str) -> List[str]:
        """
        Recursively collects all file paths of digital books within a folder.

        Args:
            folder_path (str): The path to the folder.

        Returns:
            List[str]: A list of all file paths of digital books within the folder.
        """
        book_files = []
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                if self._is_digital_book(file_path):
                    book_files.append(file_path)
        return book_files

    def _is_digital_book(self, filepath: str) -> bool:
        """
        Checks if a file is a digital book based on its file extension and MIME type.

        Args:
            filepath (str): The path to the file.

        Returns:
            bool: True if the file is a digital book, False otherwise.
        """
        # Check file extension and MIME type
        if not filepath.lower().endswith(('.pdf', '.epub', '.mobi', '.chm')):
            return False

        # Check MIME type for additional verification
        mime_type, _ = mimetypes.guess_type(filepath)
        if mime_type not in (
        'application/pdf', 'application/epub+zip', 'application/x-mobipocket-ebook', 'application/vnd.ms-htmlhelp'):
            return False

        return True

    def _process_book(self, filepath: str):
        """
        Extracts book information from a digital book file and adds it to the database.

        Args:
            filepath (str): The path to the digital book file to be processed.
        """
        try:
            title, author = self.book_info_extractor.get_book_info(filepath)
            self.db_handler.add_book(title, author)
            print(f"Processed digital book '{filepath}' - Title: '{title}', Author: '{author}'")
        except Exception as e:
            print(f"Error processing digital book '{filepath}': {e}")


if __name__ == "__main__":
    # Example usage:
    folder_path = "path/to/your/books/folder"
    db_path = "path/to/your/database.db"

    processor = BookProcessor(folder_path, db_path)
    processor.process_books()
