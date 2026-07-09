"""
Entry point: runs the full Extractor -> Categorizer -> Report crew
on a single receipt file passed via command line.

Usage:
    uv run main.py path/to/receipt.pdf
"""

import sys
from dotenv import load_dotenv

load_dotenv()

from crewai import Crew, Process
from agents import extractor_agent, categorizer_agent, report_agent
from tasks import extract_task, categorize_task, report_task


def run_expense_report(file_path: str) -> str:
    crew = Crew(
        agents=[extractor_agent, categorizer_agent, report_agent],
        tasks=[extract_task, categorize_task, report_task],
        process=Process.sequential,
        verbose=True,
    )

    result = crew.kickoff(inputs={"file_path": file_path})
    return str(result)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: uv run main.py path/to/receipt.pdf")
        sys.exit(1)

    receipt_path = sys.argv[1]
    output = run_expense_report(receipt_path)
    print("\n=== EXPENSE REPORT ===\n")
    print(output)