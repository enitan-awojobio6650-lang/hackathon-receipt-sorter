"""
Task definitions for the Expense Report pipeline.
Each task feeds its output into the next via CrewAI's context chaining.
"""

from crewai import Task
from agents import extractor_agent, categorizer_agent, report_agent

extract_task = Task(
    description=(
        "Read the receipt file at path: {file_path}. "
        "Extract the vendor name, date, total amount, currency, and any line items. "
        "Return the result as clean JSON with keys: vendor, date, amount, currency, items."
    ),
    expected_output="A JSON object with vendor, date, amount, currency, and items fields.",
    agent=extractor_agent,
)

categorize_task = Task(
    description=(
        "Using the extracted receipt data, assign it to ONE category from: "
        "Travel, Meals, Office Supplies, Software, Lodging, Other. "
        "Return the original JSON with an added 'category' field."
    ),
    expected_output="The receipt JSON with an added 'category' field.",
    agent=categorizer_agent,
    context=[extract_task],
)

report_task = Task(
    description=(
        "Using the categorized expense data, write a clean expense report. "
        "Include: a summary table (vendor, date, category, amount), "
        "a total sum, and a one-line breakdown by category. "
        "Format it in Markdown."
    ),
    expected_output="A Markdown-formatted expense report.",
    agent=report_agent,
    context=[categorize_task],
)