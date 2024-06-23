import sys
from book_processor import BookProcessor
from database import DatabaseViewer


def main(folder_path: str, db_path: str, view_db: bool):
    if view_db:
        db_viewer = DatabaseViewer(db_path)
        db_viewer.show_all_books()
    else:
        processor = BookProcessor(folder_path, db_path)
        processor.process_books()


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <folder_path> <db_path> [--view-db]")
        sys.exit(1)

    folder_path = sys.argv[1]
    db_path = sys.argv[2]
    view_db = '--view-db' in sys.argv

    main(folder_path, db_path, view_db)
