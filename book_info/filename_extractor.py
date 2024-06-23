import re
from typing import Optional, Tuple


class FilenameExtractor:
    """
    Extracts the book title and author from a given filename.
    """

    @staticmethod
    def extract_book_info(filename: str) -> Tuple[str, Optional[str]]:
        # Remove file extension
        filename = re.sub(r'\.[a-zA-Z0-9]+$', '', filename)

        # Common patterns
        patterns = [
            r'^(.*?) - (.*?)$',  # e.g., "BookTitle - Author"
            r'^(.*?) - (.*?) -',  # e.g., "BookTitle - Author - ..."
            r'^(.*?) \((.*?)\)$',  # e.g., "BookTitle (Author)"
            r'^(.*?) - (.*?) -',  # e.g., "Author - BookTitle"
            r'^(.*?) by (.*?)$',  # e.g., "BookTitle by Author"
            r'^(.*?) -- (.*?)$',  # e.g., "BookTitle -- Author"
        ]

        for pattern in patterns:
            match = re.match(pattern, filename)
            if match:
                # Return the first two matching groups
                return match.group(1).strip(), match.group(2).strip()

        # If no pattern matches, return the filename and None
        return filename.strip(), None
