"""
IVS Project 2 - Golden Calculator

@brief: This module provides functions for converting and evaluating mathematical expressions
in infix and postfix notation.

@authors: Maksim Kalutski (xkalut00)
          Volodymyr Kaznacheiev (xkazna01)
@file math_logic.py
@date 2024-24-04
"""

import re


def infix_to_postfix(expression):
    """ Converts an infix expression (standard arithmetic form) to postfix (RPN).

    Args:
        expression (str): The infix mathematical expression to convert.

    Returns:
        list: A list of tokens representing the postfix expression.
    """

    precedence = {
        '(': 0, ')': 0,  # Parentheses have the lowest precedence for stack operations
        '!': 4,  # Factorial has the highest precedence
        '^': 3,  # Exponentiation comes next
        '√': 3,  # Square root has the same precedence as exponentiation
        '*': 2,  # Multiplication
        '/': 2,  # Division
        '+': 1,  # Addition
        '-': 1,  # Subtraction
        '%': 1   # Percent
    }
    right_associative = {'^', '√', '!'}
    stack = []
    postfix = []
    previous_token = None
    for token in expression:
        if re.match(r'^[\d\.]+(?:e[+\-]?\d+)?$', token):
            postfix.append(token)
        elif token in precedence:
            if token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()
            else:
                if token == '-' and (previous_token is None or previous_token in "+-*/!^√()%"):
                    postfix.append('0')
                while (stack and stack[-1] != '(' and
                       (precedence[stack[-1]] > precedence[token] or
                        (precedence[stack[-1]] == precedence[token] and token not in right_associative))):
                    postfix.append(stack.pop())
                stack.append(token)
        previous_token = token
    while stack:
        postfix.append(stack.pop())
    return postfix


def evaluate_postfix(postfix):
    """ Evaluates a postfix expression.

    Args:
        postfix (list): The postfix expression as a list of tokens.

    Returns:
        float or str: The result of the evaluation or an error message.
    """

    stack = []
    for char in postfix:
        if re.match(r'^[\d\.]+(?:e[+\-]?\d+)?$', char):
            stack.append(float(char))
        else:
            b = stack.pop()
            if char == '+':
                a = stack.pop()
                result = plus([a, b])
            elif char == '-':
                a = stack.pop()
                result = minus(a, b)
            elif char == '*':
                a = stack.pop()
                result = mul(a, b)
            elif char == '/':
                a = stack.pop()
                if b == 0:
                    return "Error: Division by zero"
                result = div(a, b)
            elif char == '^':
                a = stack.pop()
                result = power(a, b)
            elif char == '!':
                if not b.is_integer() or b < 0:
                    return "Error: Factorial requires a non-negative integer"
                result = factorial(b)
            elif char == '√':
                if b < 0:
                    return "Error: Cannot take square root of a negative number"
                try:
                    a = stack.pop()
                    result = root(b, a)
                except IndexError:
                    result = root(b)
            elif char == '%':
                result = percent(b)
            stack.append(result)
    result = stack.pop()
    if len(stack) != 0:
        return "Error: Invalid expression"
    if result > 1e10:
        return format(result, '.2e')
    elif result % 1 == 0:
        return int(result)
    return round(result, 7)


def split_by_expression_parts(expression):
    parts = re.findall(r'[+\-*/^√!%()]|\d+\.?\d*(?:e[+\-]?\d+)?', expression)
    return parts


def evaluate_expression(expression):
    """ Evaluates a mathematical expression in infix format.

    Args:
        expression (str): The infix expression to evaluate.

    Returns:
        float or str: The result of the expression or an error message.
    """

    expression = split_by_expression_parts(expression)
    postfix = infix_to_postfix(expression)
    return evaluate_postfix(postfix)


def plus(nums):
    """Calculate the sum of a list of numbers.

    Args:
        nums (list): List of numbers to be summed.

    Returns:
        float: The sum of the numbers.
    """
    return sum(nums)


def minus(a, b):
    """Subtract b from a.

    Args:
        a (float): The number to be subtracted from.
        b (float): The number to subtract.

    Returns:
        float: The result of the subtraction.
    """
    return a - b


def mul(a, b):
    """Multiply two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The result of the multiplication.
    """
    return a * b


def div(a, b):
    """Divide a by b.

    Args:
        a (float): The dividend.
        b (float): The divisor.

    Returns:
        float: The result of the division.
    """
    return a / b


def power(a, b):
    """Raise a to the power of b.

    Args:
        a (float): The base.
        b (float): The exponent.

    Returns:
        float: The result of the exponentiation.
    """
    return a ** b


def factorial(n):
    """Calculate the factorial of a non-negative integer.

    Args:
        n (int): The non-negative integer.

    Returns:
        int: The factorial of n.
    """
    result = 1
    for i in range(1, int(n) + 1):
        result *= i
    return result


def root(a, n=2):
    """Calculate the nth root of a.

    Args:
        a (float): The number.
        n (float, optional): The degree of the root. Defaults to 2.

    Returns:
        float: The nth root of a.
    """
    return a ** (1 / n)


def percent(a):
    """Convert a percentage to its decimal equivalent.

    Args:
        a (float): The percentage value.

    Returns:
        float: The decimal equivalent of the percentage.
    """
    return a / 100
