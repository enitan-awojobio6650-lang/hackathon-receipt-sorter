Expense Report Agent

A CrewAI multi-agent pipeline that reads a receipt, extracts the details, categorizes the expense, and generates a clean expense report.

Pipeline


1.Extractor Agent — reads the receipt file (.txt, .pdf, .png, .jpg) and pulls out vendor, date, amount, and line items as JSON.
2.Categorizer Agent — assigns the expense to a category (Travel, Meals, Office Supplies, Software, Lodging, Other).
3.Report Agent — compiles everything into a Markdown expense report with a summary table and totals.
Setup
# 1. Install dependencies with uv
uv sync

# 2. Copy the env template and add your OpenRouter key
cp .env.example .env
# then edit .env and paste in your OPENROUTER_API_KEY

# 3. (If testing image receipts) install tesseract OCR on your system
#    macOS: brew install tesseract
#    Ubuntu: sudo apt install tesseract-ocr