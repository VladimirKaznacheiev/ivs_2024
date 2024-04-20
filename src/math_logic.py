import re
import math

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return None


def infix_to_postfix(expression):
    precedence = {
        '!': 4,   # Factorial has the highest precedence
        '^': 3,   # Exponentiation comes next
        '√': 3,   # Square root has the same precedence as exponentiation
        '*': 2,   # Multiplication
        '/': 2,   # Division
        '+': 1,   # Addition
        '-': 1    # Subtraction
    }
    stack = []
    postfix = []
    for char in expression:
        if char.isdigit():
            postfix.append(char)
        elif char in "+-*/!^√":
            while stack and precedence[stack[-1]] >= precedence[char]:
                postfix.append(stack.pop())
            stack.append(char)
    while stack:
        postfix.append(stack.pop())
    return postfix


def evaluate_postfix(postfix):
    stack = []
    print(postfix)
    for char in postfix:
        if char.isdigit():
            stack.append(int(char))
        else:
            b = stack.pop()
            if char == '+':
                a = stack.pop()
                result = a + b
            elif char == '-':
                a = stack.pop()
                result = a - b
            elif char == '*':
                a = stack.pop()
                result = a * b
            elif char == '/':
                a = stack.pop()
                result = a / b
            elif char == '^':
                a = stack.pop()
                result = a ** b
            elif char == '!':
                result = 1
                for i in range(1, b + 1):
                    result *= i
                     
            elif char == '√':
                result = b ** 0.5
            stack.append(result)
    result = stack[0]


    if result > 1e10:
        return format(result, '.2e')
    elif result % 1 == 0:
        return int(result)
    return round(result, 7)

def split_by_expression_parts(expression):
    parts = re.findall(r'[0-9]+|[+\-*/^√!]', expression)
    return parts

def evaluate_expression(expression):
    expression = split_by_expression_parts(expression)
    postfix = infix_to_postfix(expression)
    return evaluate_postfix(postfix)

