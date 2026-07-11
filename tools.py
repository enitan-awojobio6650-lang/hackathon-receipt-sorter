"""
Custom tools for the Expense Report Agent.
These wrap file-reading logic so the CrewAI agents can call them.
"""

import os
from crewai.tools import tool


@tool("Read Receipt File")
def read_receipt_file(file_path: str) -> str:
    """
    Reads a receipt file and returns its raw text content.
    Supports .txt, .pdf, and common image formats (.png, .jpg, .jpeg) via OCR.

    Args:
        file_path: Path to the receipt file on disk.

    Returns:
        Extracted raw text from the receipt.
    """
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".txt":
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    elif ext == ".pdf":
        import pdfplumber
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text.strip() or "No extractable text found in PDF."

    elif ext in (".png", ".jpg", ".jpeg"):
        import pytesseract
        from PIL import Image
        import platform

        if platform.system() == "Windows":
            pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

        image = Image.open(file_path)
        return pytesseract.image_to_string(image).strip() or "No text detected in image."
        
    else:
        return f"Unsupported file type: {ext}"