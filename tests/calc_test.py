"""
IVS Project 2 - Golden Calculator

@brief: Test module for the math_logic module. Contains test cases for the basic arithmetic
operations, factorial, exponentiation, and square root functions.

@author: Maksim Kalutski (xkalut00)

@file calc_test.py
@date 2024-22-04
"""

import pytest
import math

from src.math_logic import evaluate_expression


# Tests addition operations with multiple test cases using pytest parametrization.
@pytest.mark.parametrize("expression, expected", [
    ("1 + 2", 3),
    ("-1 + 1", 0),
    ("100 + 200", 300),
    ("1000000 + 1000000", 2000000),
    ("0.1 + 0.2", 0.3),
    ("-1.1 + 1.1", 0.0),
    ("1.234567 + 2.345678", 3.580245),
    ("0 + 0", 0),
    ("0 + 1", 1),
    ("1 + 0", 1),
    ("-10 + 5", -5),
])
def test_add(expression, expected):
    result = evaluate_expression(expression)
    assert result == expected, f"Expected {expected}, but got {result}"


# Tests subtraction operations with multiple test cases using pytest parametrization.
@pytest.mark.parametrize("expression, expected", [
    ("2 - 1", 1),
    ("1 - 2", -1),
    ("0 - 0", 0),
    ("0 - 1", -1),
    ("1 - 0", 1),
    ("10 - 5", 5),
    ("5 - 10", -5),
    ("0.7 - 0.4", 0.3),
    ("5.5 - 2.1", 3.4),
    ("0 - 0", 0),
    ("0 - 100000", -100000),
    ("100000 - 0", 100000),
    ("1 - 5", -4),
    ("5 - 1", 4),
    ("-1 - 5", -6),
])
def test_subtract(expression, expected):
    result = evaluate_expression(expression)
    assert result == expected, f"Expected {expected}, but got {result}"


# Tests multiplication operations with multiple test cases using pytest parametrization.
@pytest.mark.parametrize("expression, expected", [
    ("2 * 3", 6),
    ("0 * 5", 0),
    ("5 * 0", 0),
    ("-1 * 1", -1),
    ("0.5 * 2", 1.0),
    ("-0.5 * 2", -1.0),
    ("1.5 * 2.5", 3.75),
    ("0.1 * 0.2", 0.02),
    ("0 * 0", 0),
    ("0 * 100000", 0),
    ("100000 * 0", 0),
    ("1 * 5", 5),
    ("5 * 1", 5),
    ("-1 * 5", -5),
])
def test_multiply(expression, expected):
    result = evaluate_expression(expression)
    assert result == expected, f"Expected {expected}, but got {result}"


# Tests division operations with error handling for division by zero.
@pytest.mark.parametrize("expression, expected", [
    ("10 / 2", 5),
    ("9 / 3", 3),
    ("-12 / 4", -3),
    ("0 / 1", 0),
    ("1 / 2", 0.5),
    ("1 / 3", 0.3333333),
    ("10 / 4", 2.5),
    ("0 / 0", "Error: Division by zero"),
    ("100000 / 1", 100000),
    ("1 / 100000", 0.00001),
    ("1 / 5", 0.2),
    ("5 / 1", 5),
    ("-5 / 1", -5),
    ("0 / 100000", 0),
])
def test_divide(expression, expected):
    result = evaluate_expression(expression)
    assert result == expected, f"Expected {expected}, but got {result}"


# Tests factorial calculations and combinations with addition and multiplication.
@pytest.mark.parametrize("expression, expected", [
    ("0!", 1),
    ("5!", 120),
    ("3! + 2", 8),
    ("3! * 2", 12),
    ("3! + 4 * 2", 14),
    ("10!", 3628800),
    ("5!", 120),
    ("1!", 1),
    ("6! / 720", 1),
    ("2 * 0! + 3", 5),
    ("3! + 4!", 30),
    ("2^3!", 64)
])
def test_factorial(expression, expected):
    if expected is None:
        with pytest.raises(Exception):
            result = evaluate_expression(expression)
    else:
        result = evaluate_expression(expression)
        assert result == expected, f"Failed on extended factorial test with expression: {expression}"


# Tests exponentiation with nested operations and varying bases and exponents.
@pytest.mark.parametrize("expression, expected", [
    ("2 ^ 3", 8),
    ("3 ^ 4", 81),
    ("0 ^ 5", 0),
    ("5 ^ 0", 1),
    ("1 ^ 100", 1),
    ("(-4) ^ 6", 4096),
    ("(-3) ^ 3", -27),
    ("1.5 ^ 2", 2.25),
    ("2.5 ^ 1.5", 3.952847075210474),
    ("10 ^ 10", 10000000000),
    ("2 ^ 32", 4294967296),
    ("2 ^ 3 ^ 2", 512),
    ("2 * 2 ^ 3", 16),
    ("3 + 4 ^ 2", 19),
    ("18 / 2 ^ 2", 4.5),
    ("2 ^ 3", 8),
    ("3 ^ 4", 81),
    ("0 ^ 5", 0),
    ("5 ^ 0", 1),
    ("1 ^ 100", 1),
    ("1.5 ^ 2", 2.25),
    ("2.5 ^ 1.5", 3.952847075210474),
    ("10 ^ 10", 10000000000),
    ("2 ^ 32", 4294967296),
    ("2 ^ 3 ^ 2", 512),
    ("2 * 2 ^ 3", 16),
    ("3 + 4 ^ 2", 19),
    ("18 / 2 ^ 2", 4.5),
    ("4 ^ 0.5", 2),
    ("0.01 ^ 2", 0.0001),
    ("1.01 ^ 365", 37.78343433288728),
    ("2 ^ 2 ^ 3", 256),
    ("2 + 3 ^ 2 * 4", 38),
    ("0 ^ 0", 1),
])
def test_exponentiation(expression, expected):
    result = evaluate_expression(expression)
    if expected is None:
        assert result is None, f"Expected None but got {result} for {expression}"
    else:
        assert result == pytest.approx(expected), f"Failed on {expression}"


# Tests square root operations and their accuracy with pytest approximations.
@pytest.mark.parametrize("expression, expected", [
    ("2√4", 2),
    ("2√9", 3),
    ("2√16", 4),
    ("2√2", math.sqrt(2)),
    ("2√3", math.sqrt(3)),
    ("2√5", math.sqrt(5)),
    ("2√8", math.sqrt(8)),
    ("2√10000", 100),
    ("2√1000000", 1000),
    ("2√0", 0),
    ("2√1", 1),
    ("2√0.25", 0.5),
    ("2√0.81", 0.9),
    ("3 + 2√4", 5),
])
def test_sqrt(expression, expected):
    result = evaluate_expression(expression)
    if isinstance(expected, float):
        assert result == pytest.approx(expected), f"Failed on sqrt({expression})"
    else:
        assert result == expected, f"Failed on sqrt({expression})"


# Tests complex expressions involving multiple operations including parentheses and mixed operations.
@pytest.mark.parametrize("expression, expected", [
    ("(1 + 2) * (3 + 4)", 21),
    ("1 + 2 * 3 - 4 / 2", 5),
    ("(1 + 2) * (3 - 4) / 2", -1.5),
    ("2 ^ 2 + 3 * 4", 16),
    ("(2 + 3) ^ (2 - 1)", 5),
    ("2 * (3 + 4 ^ 2)", 38),
    ("(2 + 3 * 4) ^ 2", 196),
    ("0.33333 + 0.66667", 1.0),
    ("1.000001 - 0.000001", 1.0),
    ("2.000001 * 1.999999", 4.000002),
    ("(3! + 4) * 2", 20),
    ("2 ^ 3! + 4", 68),
    ("1 / 0", "Error: Division by zero"),
    ("2 ^ 0", 1),
    ("(-2) ^ 2", 4),
    ("(-2) ^ 3", -8),
    ("8 ^ (1/3)", 2),
    ("9 ^ (1/2)", 3),
    ("27 ^ (-1/3)", 1 / 3),
    ("16 ^ 0.5", 4),
])
def test_complex_expressions(expression, expected):
    result = evaluate_expression(expression)
    if isinstance(expected, str) and "Error" in expected:
        assert "Error" in result, f"Expected an error for {expression}, but got {result}"
    elif isinstance(expected, float):
        assert result == pytest.approx(expected), f"Failed on {expression} with expected {expected}"
    else:
        assert result == expected, f"Expected {expected}, but got {result}"
