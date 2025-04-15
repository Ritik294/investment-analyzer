
import fitz    # PyMuPDF

def extract_text_from_pdf(file_path):
    """Extract full text from a PDF file using PyMuPDF."""
    doc = fitz.open(file_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    doc.close()
    return full_text.strip()