from get_book_info import get_book_info_by_name
from utils import print_book_data

def process_dict(dictionary):
    for filename in dictionary:
        if filename.endswith(('.pdf', '.epub', '.mobi', '.chm')):
            title, author = get_book_info_by_name(filename)
            print_book_data(title, author)
            # Save to database or further processing
    return
