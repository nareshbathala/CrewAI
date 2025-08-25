#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from financial_researcher.crew import FinancialResearcher

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the Resarcher Crew.
    """
    inputs = {
        'compnany': 'Telsa',
    }
    
    try:
        results = FinancialResearcher().crew().kickoff(inputs=inputs)
        print(results.raw)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


if _name__ == "__main__":
    run()