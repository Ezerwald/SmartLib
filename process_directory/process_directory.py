import os

from get_book_info.get_book_info import get_book_info


def process_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith(('.pdf', '.epub', '.mobi', '.chm')):
            filepath = os.path.join(directory, filename)
            title, author = get_book_info(filepath)
            print(f"File: {filename}, Title: {title}, Author: {author}")
            # Save to database or further processing
    return
