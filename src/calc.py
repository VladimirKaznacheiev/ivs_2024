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
    precedence = {'+':1, '-':1, '*':2, '/':2}
    stack = []
    postfix = []
    for char in expression:
        if char.isdigit():
            postfix.append(char)
        elif char in "+-*/":
            while stack and precedence[stack[-1]] >= precedence[char]:
                postfix.append(stack.pop())
            stack.append(char)
    while stack:
        postfix.append(stack.pop())
    return postfix


def evaluate_postfix(postfix):
    stack = []
    for char in postfix:
        if char.isdigit():
            stack.append(int(char))
        else:
            b, a = stack.pop(), stack.pop()
            if char == '+': result = a + b
            elif char == '-': result = a - b
            elif char == '*': result = a * b
            elif char == '/': result = a / b
            stack.append(result)
    return stack[0]


def evaluate_expression(expression):
    postfix = infix_to_postfix(expression.replace(" ", ""))
    return evaluate_postfix(postfix)

