import requests
from configs import goodreads_api_key


def fetch_book_info(query, key=goodreads_api_key):
    """Fetches book info from different online databases."""
    # First try Google Books
    title, author = fetch_book_info_googlebooks(query)
    if title and author:
        return title, author

    # Then try Open Library
    title, author = fetch_book_info_openlibrary(query)
    if title and author:
        return title, author

    # Then try Goodreads
    if key:
        title, author = fetch_book_info_goodreads(query, key)
        if title and author:
            return title, author

    # If all else fails
    return None, None


def fetch_book_info_googlebooks(query):
    """Fetches book info from Google Books API."""
    api_url = f'https://www.googleapis.com/books/v1/volumes?q={query}'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if 'items' in data and len(data['items']) > 0:
            item = data['items'][0]['volumeInfo']
            title = item.get('title')
            authors = item.get('authors', [])
            author = ', '.join(authors) if authors else None
            return title, author
    return None, None


def fetch_book_info_openlibrary(query):
    """Fetches book info from OpenLibrary API."""
    api_url = f'https://openlibrary.org/search.json?q={query}'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if 'docs' in data and len(data['docs']) > 0:
            doc = data['docs'][0]
            title = doc.get('title')
            author_list = doc.get('author_name', [])
            author = ', '.join(author_list) if author_list else None
            return title, author
    return None, None


def fetch_book_info_goodreads(query, api_key):
    """Fetches book info from Good Reads API."""
    if not api_key:
        return None, None
    api_url = f'https://www.goodreads.com/search/index.xml?key={api_key}&q={query}'
    response = requests.get(api_url)
    if response.status_code == 200:
        # Goodreads returns XML, so you need to parse it
        import xml.etree.ElementTree as ET
        root = ET.fromstring(response.content)
        work = root.find('.//work')
        if work is not None:
            best_book = work.find('best_book')
            if best_book is not None:
                title = best_book.find('title').text
                author = best_book.find('.//author/name').text
                return title, author
    return None, None
