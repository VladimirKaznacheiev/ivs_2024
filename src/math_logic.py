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
                result = squareroot(b)
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
    return sum(nums)


def minus(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def power(a, b):
    return a ** b


def factorial(n):
    result = 1
    for i in range(1, int(n) + 1):
        result *= i
    return result


def squareroot(a):
    return a ** 0.5


def percent(a):
    return a / 100
