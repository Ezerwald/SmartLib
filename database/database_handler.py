import sqlite3
from typing import Tuple, List


class DatabaseHandler:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.connection = self._create_connection()
        self._create_table()

    def _create_connection(self):
        try:
            conn = sqlite3.connect(self.db_path)
            return conn
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def _create_table(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL
                )
            """)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def add_book(self, title: str, author: str):
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error adding book to database: {e}")

    def get_all_books(self) -> List[Tuple[int, str, str]]:
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT id, title, author FROM books")
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving books from database: {e}")
            return []

    def close_connection(self):
        if self.connection:
            self.connection.close()
