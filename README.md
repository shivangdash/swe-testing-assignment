# SWE Testing Assignment: Quick-Calc

## Project Description

Quick-Calc is a simple calculator application implemented in Python. It supports basic arithmetic operations: addition, subtraction, multiplication, and division, with proper handling of division by zero. It also includes a clear function to reset the calculator.

## Setup Instructions

1. Ensure you have Python 3 installed.

2. Clone the repository: `git clone https://github.com/yourusername/swe-testing-assignment.git`

3. Navigate to the directory: `cd swe-testing-assignment`

4. No additional dependencies are required for the core functionality.

## How to Run the Application

Run the CLI version: `python main.py`

## How to Run Tests

Install pytest if not already installed: `pip install pytest`

Run all tests: `pytest`

## Testing Framework Research

For Python, two popular testing frameworks are pytest and unittest.

Pytest is a modern testing framework that is easy to use, with simple syntax, powerful fixtures, and extensive plugins. It supports parametrized tests and has good integration with CI/CD. However, it requires installation and might have a learning curve for complex setups.

Unittest is Python's built-in testing framework, based on JUnit. It doesn't require installation, is familiar to those from Java background, and integrates well with the standard library. However, it can be more verbose and less flexible than pytest.

I chose pytest because of its simplicity and powerful features, making it ideal for this project.