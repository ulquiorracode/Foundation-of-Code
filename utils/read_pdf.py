import sys
from PyPDF2 import PdfReader

try:
    reader = PdfReader(sys.argv[1])
    with open("pdf_text.txt", "w", encoding="utf-8") as f:
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            f.write(f"--- Page {i+1} ---\n")
            f.write(text + "\n")
except Exception as e:
    print(f"Error: {e}")
