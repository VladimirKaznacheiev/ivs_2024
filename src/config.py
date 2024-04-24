# config.py

APP_TITLE = 'Calculator'
APP_RESOLUTION = '400x600'
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
BUTTONS_COLOR = "#f4f6eb"
DISPLAY_COLOR = "#e2e5d8"

# Define keyboard bindings
KEYBOARD_BINDINGS = {
    '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '0': '0',
    '+': '+', '-': '-', '*': '×', '/': '÷', '.': '.', '^': '^', '!': '!',
    '(': '(', ')': ')', '<BackSpace>': 'DEL', '<Return>': '=', '<Delete>': 'AC',
    # Numpad keys
    '<KP_End>': '1', '<KP_Down>': '2', '<KP_Next>': '3', '<KP_Left>': '4',
    '<KP_Begin>': '5', '<KP_Right>': '6', '<KP_Home>': '7', '<KP_Up>': '8',
    '<KP_Prior>': '9', '<KP_Insert>': '0', '<KP_Decimal>': '.', '<KP_Add>': '+',
    '<KP_Subtract>': '-', '<KP_Multiply>': '*', '<KP_Divide>': '/', '<KP_Enter>': '=',
    '<KP_0>': '0', '<KP_1>': '1', '<KP_2>': '2', '<KP_3>': '3', '<KP_4>': '4',
    '<KP_5>': '5', '<KP_6>': '6', '<KP_7>': '7', '<KP_8>': '8', '<KP_9>': '9',
}
