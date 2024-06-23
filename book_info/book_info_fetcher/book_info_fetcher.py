from typing import Optional, Tuple
from .google_books_fetcher import GoogleBooksFetcher
from .open_library_fetcher import OpenLibraryFetcher


class BookInfoFetcher:
    """Class to fetch book information from various online databases."""

    @staticmethod
    def get_book_info_from_online_databases(query: str) -> Optional[Tuple[str, str]]:
        """Fetches book info from different online databases."""
        # Check in Google Books database
        title, author = GoogleBooksFetcher.fetch_book_info(query)
        if title and author:
            return title, author

        # Check in Open Library database
        title, author = OpenLibraryFetcher.fetch_book_info(query)
        if title and author:
            return title, author

        return None
