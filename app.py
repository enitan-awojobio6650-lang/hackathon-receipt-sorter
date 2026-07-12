"""
Gradio front-end: upload a receipt, get back a generated expense report.

Usage:
    uv run app.py
"""

import os

import gradio as gr
from dotenv import load_dotenv
from main import run_expense_report

load_dotenv()


def process_receipt(file):
    if file is None:
        return "Please upload a receipt file (.txt, .pdf, .png, or .jpg)."
    try:
        return run_expense_report(file.name)
    except Exception as e:
        return f"Error processing receipt: {e}"


demo = gr.Interface(
    fn=process_receipt,
    inputs=gr.File(label="Upload Receipt", file_types=[".txt", ".pdf", ".png", ".jpg", ".jpeg"]),
    outputs=gr.Markdown(label="Generated Expense Report"),
    title="Expense Report Agent",
    description="Upload a receipt and let the agent crew extract, categorize, and summarize it.",
    demo = gr.Interface(
    title="🧾 Expense Report Agent",
    description="Upload a receipt and let the agent crew extract, categorize, and summarize it.",
    theme=gr.themes.Soft(primary_hue="orange"),
)
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 7860)))