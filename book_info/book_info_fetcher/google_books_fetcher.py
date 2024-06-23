import requests
from typing import Optional, Tuple


class GoogleBooksFetcher:
    """Fetches book info from Google Books API."""

    @staticmethod
    def fetch_book_info(query: str) -> Optional[Tuple[str, str]]:
        api_url = f'https://www.googleapis.com/books/v1/volumes?q={query}'
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()
            if 'items' in data and data['items']:
                item = data['items'][0]['volumeInfo']
                title = item.get('title')
                authors = item.get('authors', [])
                author = ', '.join(authors) if authors else None
                return title, author
        except requests.RequestException as e:
            print(f"Google Books API request failed: {e}")
        return None, None
