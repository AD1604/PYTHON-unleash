import tkinter as tk
from tkinter import ttk

class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Simple Calculator')
        self.geometry('300x400')

        # Entry widget to display input and results
        self.entry = tk.Entry(self, width=30, font=('Arial', 14))
        self.entry.grid(row=0, column=0, columnspan=4, pady=10)

        # Buttons for digits and operations
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (text, row, column) in buttons:
            ttk.Button(self, text=text, command=lambda t=text: self.on_button_click(t)).grid(row=row, column=column, padx=5, pady=5)

    def on_button_click(self, text):
        if text == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, 'Error')
        else:
            self.entry.insert(tk.END, text)

if __name__ == '__main__':
    app = CalculatorApp()
    app.mainloop()
