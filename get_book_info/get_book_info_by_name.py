from .extract_book_info_from_filename import extract_info
from .fetch_book_info_from_online_databases import fetch_book_info
from utils import log_book_data


def get_book_info_by_name(filename):
    # Check if author and title are mentioned in filename
    title, author = extract_info(filename)
    log_book_data(title, author)

    if not title or not author:
        # Check if author and title are mentioned in online databases
        title, author = fetch_book_info(title if title else filename)
        log_book_data(title, author)

    if not title:
        print('No title found')
        title = filename
    if not author:
        print('No author found')
        author = "No author found"

    return title, author
