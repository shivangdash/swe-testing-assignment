# Testing Strategy for Quick-Calc

## Testing Strategy

I tested the core calculation functions (add, subtract, multiply, divide) with unit tests, covering normal cases, edge cases like division by zero, negative numbers, decimals, and large numbers. For integration tests, I tested the interaction between user inputs and the calculator state, simulating full operations and clear functionality. I did not test non-functional aspects like performance or UI aesthetics, as the focus is on functional correctness.

## Lecture Concepts

- **Testing Pyramid**: My test suite has a base of 8 unit tests (bottom layer), and 3 integration tests (middle layer). No UI tests (top layer) as there's no GUI.

- **Black-box vs White-box Testing**: Unit tests are white-box as they test the internal functions directly. Integration tests are black-box as they test the behavior through inputs without knowing internals.

- **Functional vs Non-Functional Testing**: All tests are functional, testing what the calculator does. No non-functional tests like load or usability.

- **Regression Testing**: The test suite can be run after changes to ensure no regressions; for example, if I modify the divide function, the tests will catch if division by zero handling breaks.

## Test Results Summary

| Test Name | Type | Status |
|-----------|------|--------|
| test_add | Unit | Pass |
| test_subtract | Unit | Pass |
| test_multiply | Unit | Pass |
| test_divide | Unit | Pass |
| test_divide_by_zero | Unit | Pass |
| test_large_numbers | Unit | Pass |
| test_decimal_operations | Unit | Pass |
| test_full_addition | Integration | Pass |
| test_clear_after_calculation | Integration | Pass |
| test_division_by_zero_integration | Integration | Pass |