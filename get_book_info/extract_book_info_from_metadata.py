from PyPDF2 import PdfFileReader


def extract_pdf_metadata(filepath):
    """Extract metadata from a PDF file"""
    with open(filepath, 'rb') as f:
        reader = PdfFileReader(f)
        info = reader.getDocumentInfo()
        title = info.title if info.title else None
        author = info.author if info.author else None
        return title, author
