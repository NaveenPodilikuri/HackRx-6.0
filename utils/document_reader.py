import fitz  # PyMuPDF
import requests
from io import BytesIO

def extract_text_from_pdf(url: str) -> str:
    response = requests.get(url)
    response.raise_for_status()
    doc = fitz.open(stream=BytesIO(response.content), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text
