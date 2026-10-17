# Triangle Classifier

## Overview

This project validates and classifies triangles using three side lengths. It was developed in Python and includes unit tests and customer acceptance tests.

The program checks whether the side lengths form a valid triangle, classifies valid triangles as equilateral, isosceles, or scalene, and identifies right triangles so the stained-glass studio knows when corner reinforcement is needed.

## Requirements

- Python 3.14 or a compatible Python 3 version.
- pytest for running the tests.

## Setup

Install the test dependency:

```bash
python -m pip install -r requirements.txt
```

## Running the Tests

Run the complete test suite:

```bash
python -m pytest -v
```

The project includes unit tests in `test_triangle.py` and customer acceptance tests in `test_acceptance.py`.

## Customer Requirements

- Validate three side lengths before approving a triangle for construction.
- Reject invalid and degenerate triangles.
- Classify valid triangles correctly.
- Identify right triangles for reinforced corners.
- Handle invalid dimensions without crashing.

## Copilot Review Log

I used GitHub Copilot as an assistant while developing `triangle.py` and `test_triangle.py`. I reviewed its suggestions rather than accepting everything automatically.

### Accepted Suggestions

- I accepted Copilot's suggestions for the function definitions (`def` lines), including the parameters for `is_valid_triangle(a, b, c)` and `classify_triangle(a, b, c)`. The suggested parameters matched the requirement to accept three side lengths.
- I used Copilot's suggestions when writing some of the comments and docstrings to explain what the code does.

### Edited Suggestions

- Copilot suggested the `if` statements for classifying triangles, but its initial suggestion did not include the scalene classification. I edited the code to include a separate case for scalene triangles, where all three side lengths are different.
- I reviewed the classification logic to make sure the conditions covered equilateral, isosceles, and scalene triangles.

### Rejected Suggestions

- Copilot suggested an incorrect `if` statement in `is_valid_triangle`. I rejected that suggestion because it did not correctly check whether the three side lengths formed a valid triangle. I kept the validation logic that checks for positive side lengths and applies the triangle inequality: the sum of any two sides must be greater than the third side.

### Testing and Verification

- I used Copilot to help generate unit tests in `test_triangle.py`, then reviewed the test cases.
- I included tests for zero and negative side lengths, degenerate triangles, the three main triangle classifications, right triangles, and floating-point tolerance.
- I added tests for different permutations of right-triangle side lengths to verify that the classification does not depend on the order of the inputs.
- I ran `python -m pytest -v` and verified that all 39 unit and acceptance tests passed.
- I wrote test_acceptance.py myself without using GitHub Copilot, following the assignment requirements.

### Reflection

Copilot helped me write code more efficiently, but its suggestions were not always complete or correct. Reviewing and testing the code helped me identify missing classification logic and reject an incorrect validation condition. This showed me why generated code should be checked against the requirements instead of being accepted automatically.