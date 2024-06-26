"""
IVS Project 2 - Golden Calculator

@brief: Contains the main class CalculatorApp, which is responsible for creating the GUI
of the calculator and handling the logic for button clicks and expression evaluation.
The CalculatorApp class uses the tkinter library to create the GUI elements, such as
the display and buttons, and defines the layout of the calculator.

@authors: Maksim Kalutski (xkalut00)
          Volodymyr Kaznacheiev (xkazna01)
@file app.py
@date 2024-24-04
"""

import tkinter as tk
from tkinter import font
from math_logic import evaluate_expression
import config
from tkinter import messagebox


class CalculatorApp:
    """ A simple calculator application using tkinter.

    This class handles the creation of the calculator's GUI, including the display and buttons,
    as well as the logic for button clicks and expression evaluation.

    Attributes:
        display (tk.Entry): The tkinter Entry widget used for displaying the current expression.
        window (tk.Tk): The main tkinter window of the application.
        current_expression (str): The current mathematical expression entered by the user.
    """

    def __init__(self):
        """ Initialize the CalculatorApp with a main window and layout configurations. """
        self.display = None
        self.window = tk.Tk()
        self.window.title(config.APP_TITLE)
        self.window.geometry(config.APP_RESOLUTION)
        self.current_expression = ""
        self.create_display_frame()
        self.create_buttons_frame()
        self.bind_keyboard_events()
    
    def show_help(self):
        messagebox.showinfo("Help", "Calculator Usage Instructions:\n\n"
                                    "Use the numeric keys to enter values.\n"
                                    "Press 'AC' to clear the display.\n"
                                    "Press 'DEL' to delete the last entry.\n"
                                    "To use the square root, press '√' followed by the number (e.g., '√9').\n"
                                    "To calculate an nth root, type the degree followed by '√' and the number (e.g., '3√8').\n"
                                    "If no number precedes '√', it defaults to square root.\n"
                            )

    def create_display_frame(self):
        """ Creates the display area where the calculation expression is shown. """
        self.display = tk.Entry(self.window, font=config.DIGITS_FONT_STYLE, bg=config.DISPLAY_COLOR, justify=tk.RIGHT,
                                borderwidth=0)
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew")

        self.window.grid_rowconfigure(0, weight=1)
        for i in range(4):
            self.window.grid_columnconfigure(i, weight=1)

    def create_buttons_frame(self):
        """ Creates the button layout for the calculator. """
        buttons_frame = tk.Frame(self.window)
        buttons_frame.grid(row=1, column=0, columnspan=5, sticky="nsew")
        self.window.grid_rowconfigure(1, weight=1)
        for i in range(4):
            self.window.grid_columnconfigure(i, weight=1)

        BUTTONS_LAYOUT = [
            # (Button label, row, column)
            # Defines the layout and properties of each button
            ('AC', 1, 0), ('DEL', 1, 1), ('(', 1, 2), (')', 1, 3), ('?', 1, 4),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('÷', 2, 3), ('!', 2, 4),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('×', 3, 3), ('^', 3, 4),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3), ('√', 4, 4),
            ('0', 5, 0), ('.', 5, 1), ('%', 5, 2), ('+', 5, 3), ('=', 5, 4)
        ]

        for button_text, row, col in BUTTONS_LAYOUT:
            button = tk.Button(buttons_frame, text=button_text, bg=config.BUTTONS_COLOR, borderwidth=0,
                               highlightbackground=config.BUTTONS_COLOR,
                               command=lambda text=button_text: self.on_button_click(text))
            button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        for i in range(1, 6):
            buttons_frame.rowconfigure(i, weight=1)
        for i in range(5):
            buttons_frame.columnconfigure(i, weight=1)

    def bind_keyboard_events(self):
        # Bind keyboard events
        for key, button_text in config.KEYBOARD_BINDINGS.items():
            self.window.bind(key, lambda event, text=button_text: self.on_button_click(text))

    @property
    def operation_acceptable(self):
        """ Checks if the last character of the current expression allows an operation. """
        if not self.current_expression.strip():
            return True
        last_char = self.current_expression.strip()[-1]
        return last_char.isdigit() or last_char == ')'

    def on_button_click(self, button_text):
        """ Handles the logic for when a button is clicked. """
        if button_text in {'AC', 'DEL', '='}:
            if button_text == 'AC':
                self.current_expression = ""
            elif button_text == 'DEL':
                trimmed = self.current_expression.rstrip()
                if trimmed and (trimmed[-1].isdigit() or trimmed[-1] in '.()'):
                    self.current_expression = trimmed[:-1]
                elif len(trimmed) > 1:
                    self.current_expression = trimmed[:-3]
            elif button_text == '=':
                self.evaluate_expression_ui()
        else:
            if not button_text.isnumeric() and button_text not in ['.', '(', ')', '√'] and not self.operation_acceptable:
                return

            if button_text in {'+', '-', '×', '÷'}:
                button_text = ' ' + (button_text.replace('×', '*').replace('÷', '/')) + ' '
            elif button_text == '√':
                if not self.current_expression.strip() or not self.current_expression.strip()[-1].isdigit():
                    button_text = '2'+button_text
            elif button_text == '?':
                self.show_help()
                return
            elif button_text == '!':
                button_text = '! '
            self.current_expression += button_text

        self.update_display()

    def evaluate_expression_ui(self):
        """ Evaluates the mathematical expression entered by the user. """
        expression = self.current_expression.replace('×', '*').replace('÷', '/')
        try:
            result = str(evaluate_expression(expression))
            self.current_expression = result
        except ZeroDivisionError:
            self.current_expression = "Error: Division by zero"
        except Exception as e:
            print(e)
            self.current_expression = "Error"
        finally:
            self.update_display()

    def update_display(self):
        """ Updates the calculator's display with the current expression. """

        self.display.delete(0, tk.END)
        self.display.insert(0, self.current_expression)

    def run(self):
        """ Starts the calculator application. """
        self.window.mainloop()


if __name__ == '__main__':
    app = CalculatorApp()
    app.run()
