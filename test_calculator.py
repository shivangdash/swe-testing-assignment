# test_calculator.py

import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(5, 3) == 8
    assert add(-1, 1) == 0
    assert add(0.5, 0.5) == 1.0

def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(4, 10) == -6
    assert subtract(5.5, 2.5) == 3.0

def test_multiply():
    assert multiply(6, 7) == 42
    assert multiply(-2, 3) == -6
    assert multiply(0.5, 2) == 1.0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5
    assert divide(-6, 3) == -2

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Division by zero"):
        divide(5, 0)

def test_large_numbers():
    assert add(1000000, 2000000) == 3000000
    assert multiply(1000, 1000) == 1000000

def test_decimal_operations():
    assert add(1.5, 2.5) == 4.0
    assert divide(5, 2) == 2.5