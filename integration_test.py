# integration_test.py

import pytest
from calculator import Calculator

def test_full_addition():
    calc = Calculator()
    calc.input_number(5)
    calc.input_operation('+')
    calc.input_number(3)
    calc.calculate()
    assert calc.get_display() == '8.0'

def test_clear_after_calculation():
    calc = Calculator()
    calc.input_number(5)
    calc.input_operation('+')
    calc.input_number(3)
    calc.calculate()
    assert calc.get_display() == '8.0'
    calc.clear()
    assert calc.get_display() == '0'

def test_division_by_zero_integration():
    calc = Calculator()
    calc.input_number(5)
    calc.input_operation('/')
    calc.input_number(0)
    with pytest.raises(ValueError, match="Division by zero"):
        calc.calculate()