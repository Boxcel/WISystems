import tkinter as tk

class NumberPad(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Number Pad")
        self.geometry("300x400")
        self.create_widgets()

    def create_widgets(self):
        self.entry = tk.Entry(self, width=16, font=('Arial', 24), bd=8, insertwidth=2, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'Clear', 'Enter', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            action = lambda x=button: self.click_event(x)
            tk.Button(self, text=button, padx=20, pady=20, font=('Arial', 18), command=action).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def click_event(self, key):
        if key == 'Clear':
            self.entry.delete(0, tk.END)
        elif key == 'Enter':
            try:
                # Evaluate the expression and display the result
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, key)

if __name__ == "__main__":
    app = NumberPad()
    app.mainloop()