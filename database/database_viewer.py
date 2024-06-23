from .database_handler import DatabaseHandler


class DatabaseViewer:
    def __init__(self, db_path: str):
        self.db_handler = DatabaseHandler(db_path)

    def show_all_books(self):
        books = self.db_handler.get_all_books()
        if not books:
            print("No books found in the database.")
            return

        print(f"{'ID':<5} {'Title':<50} {'Author':<30}")
        print("=" * 85)
        for book in books:
            book_id, title, author = book
            print(f"{book_id:<5} {title:<50} {author:<30}")

        self.db_handler.close_connection()


if __name__ == "__main__":
    db_viewer = DatabaseViewer("path/to/your/database.db")
    db_viewer.show_all_books()
