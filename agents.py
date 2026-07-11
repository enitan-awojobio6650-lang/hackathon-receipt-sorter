import os
from dotenv import load_dotenv
from crewai import Agent, LLM
from tools import read_receipt_file

load_dotenv()

llm = LLM(
    model=os.getenv("MODEL_NAME", "openrouter/tencent/hy3:free"),
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

extractor_agent = Agent(
    role="Receipt Data Extractor",
    goal="Accurately extract vendor, date, amount, and line items from receipts.",
    backstory=(
        "You are a highly skilled data-entry agent specialist who processes thousands of receipts daily. "
        "You never miss a number and always double-check your totals."
    ),
    tools=[read_receipt_file],
    llm=llm,
    verbose=True,
)

categorizer_agent = Agent(
    role="Expense categorizer",
    goal="Assign each extracted expense to the correct categories (e.g. Travel, Meals, Office Supplies, Software, Other).",
    backstory=(
        "You are a highly skilled finance expert who knows standard expense categories and can classify any purchase quickly and consistently."
    ),
    llm=llm,
    verbose=True,
)

report_agent = Agent(
    role="Expense Report Writer",
    goal="Compile categorized expenses into a clean, clear, readable expense report with totals.",
    backstory=(
        "You are a highly skilled finance report writer who produces clear, well-formatted summaries that managers can approve in seconds."
    ),
    llm=llm,
    verbose=True,
)