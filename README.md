# Solve 2025

This Python script finds a mathematical expression that evaluates to a specified target value (2025 by default) using a predefined set of numbers and operations.


## How It Works
1. The script uses an **iterative depth-first search (DFS)** approach to explore all possible combinations of numbers and operations.
2. For each state, it evaluates the current expression and checks if it matches the target value within a given tolerance.
3. Operations are applied safely to handle edge cases like division by zero and invalid exponentiation.
4. If an expression evaluates to the target, it prints the result and stops execution.

## Output
If a valid expression is found, the script prints:
```
Expression Found!
Expression: ((((1 - 4) * 5) * 3) ** 2) = (-45)^2 = 2025
Solution: 2025.0
```
If no expression matches the target, it outputs:
```
No expression found.
```

## Usage
1. Run the script in your terminal:
   ```bash
   python solution.py
   ```
