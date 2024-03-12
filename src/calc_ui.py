import tkinter as tk


class CalculatorApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Calculator')
        self.window.geometry('400x600')
        self.window.resizable(0, 0)

    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    app = CalculatorApp()
    app.run()
