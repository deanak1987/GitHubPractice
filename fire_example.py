import random

import fire
from typing import List, Optional
from datetime import datetime


class DataProcessor:
    """A sample class demonstrating Python Fire integration for data processing tasks."""

    def __init__(self, data_dir: str = "./data"):
        self.data_dir = data_dir

    def process_text(
        self, text: str, uppercase: bool = False, reverse: bool = False
    ) -> str:
        """Process a text string with various operations.

        Args:
            text: Input text to process
            uppercase: Convert text to uppercase if True
            reverse: Reverse the text if True
        """
        result = text
        if uppercase:
            result = result.upper()
        if reverse:
            result = result[::-1]
        return result

    def analyze_numbers(self, numbers: List[float], operation: str = "mean") -> float:
        """Perform statistical analysis on a list of numbers.

        Args:
            numbers: List of numbers to analyze
            operation: Type of analysis ('mean', 'sum', 'max', 'min')
        """
        if not numbers:
            raise ValueError("Number list cannot be empty")

        operations = {
            "mean": lambda x: sum(x) / len(x),
            "sum": sum,
            "max": max,
            "min": min,
        }

        if operation not in operations:
            raise ValueError(
                f"Unknown operation. Choose from: {', '.join(operations.keys())}"
            )

        return operations[operation](numbers)

    def flip_coins(self, number) -> Optional[list[str]]:
        """Perform a number of coin flips and return results.

        Args:
            number: Number of times to flip coin
        """

        if number < 1:
            return None
        else:
            results = []
            for _ in range(number):
                results.append("Heads" if random.random() > 0.5 else "Tails")
            return results

    def log_operation(self, operation_name: str, status: str = "success") -> None:
        """Log an operation with timestamp."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(
            f"[{timestamp}] Operation '{operation_name}' completed with status: {status}"
        )


def example_usage():
    processor = DataProcessor()

    # Example 1: Text processing
    text_result = processor.process_text(
        "Hello, Python Fire!", uppercase=True, reverse=True
    )
    print("Text Processing Result:", text_result)

    # Example 2: Number analysis
    numbers = [23.5, 42.1, 15.8, 31.9, 27.6]
    mean_result = processor.analyze_numbers(numbers, "mean")
    max_result = processor.analyze_numbers(numbers, "max")
    print(f"Number Analysis Results:\nMean: {mean_result}\nMax: {max_result}")

    # Example 3: Coin flipping
    flips = 5
    flip_results = processor.flip_coins(flips)
    print(f"Coin flip Results: {flip_results}")

    # Example 4: Logging
    print("\nLogging operation.")
    processor.log_operation("data_analysis")


if __name__ == "__main__":
    print("Demo of Python Fire")
    fire.Fire(DataProcessor)
    print("\nDemo of program in action.")
    example_usage()
