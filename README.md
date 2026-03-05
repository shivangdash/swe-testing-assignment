# SWE Testing Assignment: Quick-Calc

## Project Description

Quick-Calc is a simple calculator application implemented in Python. It supports basic arithmetic operations: addition, subtraction, multiplication, and division, with proper handling of division by zero. It also includes a clear function to reset the calculator.

## Setup Instructions

1. Ensure you have Python 3 installed.

2. Clone the repository: `git clone https://github.com/shivangdash/swe-testing-assignment.git`

3. Navigate to the directory: `cd swe-testing-assignment`

4. No additional dependencies are required for the core functionality.

## How to Run the Application

Run the CLI version: `python main.py`

## Usage

The calculator is a command-line interface application. It accepts input one at a time and updates the display after each input.

### Input Types:
- **Numbers**: Enter digits (e.g., `5`, `10`, `3.5`)
- **Operations**: `+`, `-`, `*`, `/`
- **Calculate**: `=`
- **Clear**: `C` (resets to 0)
- **Quit**: `Q`

### Example Usage:
```
Quick-Calc CLI
Enter numbers and operations (+, -, *, /), = to calculate, C to clear, Q to quit
Input: 5
Display: 5
Input: +
Display: 5
Input: 3
Display: 3
Input: =
Display: 8.0
Input: C
Display: 0
Input: 10
Display: 10
Input: *
Display: 10
Input: 2
Display: 2
Input: =
Display: 20.0
```

## How to Run Tests

Install pytest if not already installed: `pip install pytest`

Run all tests: `pytest`

## Testing Framework Research

For Python, two popular testing frameworks are pytest and unittest.

Pytest is a modern testing framework that is easy to use, with simple syntax, powerful fixtures, and extensive plugins. It supports parametrized tests and has good integration with CI/CD. However, it requires installation and might have a learning curve for complex setups.

Unittest is Python's built-in testing framework, based on JUnit. It doesn't require installation, is familiar to those from Java background, and integrates well with the standard library. However, it can be more verbose and less flexible than pytest.

I chose pytest because of its simplicity and powerful features, making it ideal for this project.