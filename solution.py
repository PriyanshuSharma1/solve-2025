import itertools
from math import isclose
from collections import deque

TARGET_VALUE = 2025
NUMBERS = [1, 2, 3, 4, 5]
OPERATIONS = ["+", "-", "*", "/", "**"]
TOLERANCE = 1e-9


def safe_evaluate(x, y, operator):
    """
    Perform arithmetic operations safely, avoiding issues like division by zero
    or invalid exponentiation.
    """
    try:
        if operator == "+":
            return x + y
        elif operator == "-":
            return x - y
        elif operator == "*":
            return x * y
        elif operator == "/":
            if abs(y) < TOLERANCE:
                return None
            return x / y
        elif operator == "**":
            if x < 0 and not isclose(y, int(y), abs_tol=TOLERANCE):
                return None
            return x ** y
    except Exception:
        return None


def find_expression(target, numbers, operations):
    """
    Iteratively search for an expression using depth-first search (DFS).
    Each state is a tuple of (value, expression, remaining numbers).
    """
    stack = deque()

    # Initialize stack with single numbers
    for num in numbers:
        remaining = list(numbers)
        remaining.remove(num)
        stack.append((float(num), str(num), remaining))

    while stack:
        current_value, current_expr, remaining_numbers = stack.pop()

        if isclose(current_value, target, abs_tol=TOLERANCE):
            print("Expression Found!")
            print(f"Expression: {current_expr}")
            print(f"Solution: {current_value}")
            return

        # Expand current state with all possible operations and remaining numbers
        for next_num in remaining_numbers:
            new_remaining = list(remaining_numbers)
            new_remaining.remove(next_num)

            for op in operations:
                result = safe_evaluate(current_value, next_num, op)
                if result is not None:
                    stack.append((result, f"({current_expr} {op} {next_num})", new_remaining))

                # For non-commutative operations, try reversing operands
                if op in {"-", "/", "**"}:
                    reverse_result = safe_evaluate(next_num, current_value, op)
                    if reverse_result is not None:
                        stack.append((reverse_result, f"({next_num} {op} {current_expr})", new_remaining))

    print("No expression found.")


if __name__ == "__main__":
    find_expression(TARGET_VALUE, NUMBERS, OPERATIONS)
