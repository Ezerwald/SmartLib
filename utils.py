# Define the column widths
filename_width = 60
title_width = 40
author_width = 20


def log_book_data(title, author):
    print(f"{title:<{title_width}} {author:<{author_width}}")
    return


def print_book_data(filename, title, author):
    print(f"{filename:<{filename_width}} {title:<{title_width}} {author:<{author_width}}")
