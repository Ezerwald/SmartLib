import requests
from typing import Optional, Tuple


class OpenLibraryFetcher:
    """Fetches book info from OpenLibrary API."""

    @staticmethod
    def fetch_book_info(query: str) -> Optional[Tuple[str, str]]:
        api_url = f'https://openlibrary.org/search.json?q={query}'
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()
            if 'docs' in data and data['docs']:
                doc = data['docs'][0]
                title = doc.get('title')
                author_list = doc.get('author_name', [])
                author = ', '.join(author_list) if author_list else None
                return title, author
        except requests.RequestException as e:
            print(f"OpenLibrary API request failed: {e}")
        return None, None
