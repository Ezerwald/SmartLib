import re


def extract_info(filename):
    # Remove file extension
    filename = re.sub(r'\.[a-zA-Z0-9]+$', '', filename)

    # Common patterns
    patterns = [
        r'^(.*?)- (.*)$',  # e.g., "BookTitle - Author"
        r'^(.*?)- (.*?)-',  # e.g., "BookTitle - Author - ..."
        r'^(.*?)\((.*?)\)$',  # e.g., "BookTitle (Author)"
        r'^(.*?)- (.*?)-',  # e.g., "Author - BookTitle"
        r'^(.*?)( by )(.*?)$',  # e.g., "BookTitle by Author"
        r'^(.*?)(--)(.*?)$',  # e.g., "BookTitle -- Author"
    ]
    for pattern in patterns:
        match = re.match(pattern, filename)
        if match:
            return match.groups()

    # If no pattern matches
    return filename, None

