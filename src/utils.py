import PyPDF2

def extract_text_from_pdf(file_path):
    """
    Reads the text from a PDF file and returns it as a single string.
    """
    text = []
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text.append(page.extract_text())
    return "\n".join(filter(None, text))
