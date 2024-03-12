import pytest
from src.calc import add, subtract, multiply, divide


def test_addition():
    assert add(3, 4) == 7
    assert add(3, -4) == -1


def test_subtraction():
    assert subtract(3, 4) == -1
    assert subtract(3, -4) == 7


def test_multiplication():
    assert multiply(3, 4) == 12
    assert multiply(3, -4) == -12


def test_division():
    assert divide(12, 4) == 3
    assert divide(12, -4) == -3
    assert divide(12, 0) == "Error! Division by zero."
