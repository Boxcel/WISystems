import tkinter as tk
import subprocess
class StartPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Welcome")
        self.geometry("300x400")
        self.create_widgets()

    def create_widgets(self):
        welcome_label = tk.Label(self, text="Welcome to WISystems Calculator", font=('Arial', 18))
        welcome_label.pack(pady=50)

        start_button = tk.Button(self, text="Start Number Pad", font=('Arial', 18), command=self.start_calculator)
        start_button.pack(pady=20)

        graph_button = tk.Button(self, text="Start Graphing Calculator", font=('Arial', 18), command=self.start_graphing_calculator)
        graph_button.pack(pady=20)

    def start_calculator(self):
        self.destroy()
        app = NumberPad()
        app.mainloop()

    def start_graphing_calculator(self):
        self.destroy()
        self.after(0, self.open_graphing_calculator)

    def open_graphing_calculator(self):
        subprocess.Popen(["python", "WI_Systems_Graphing_Ui.py"])

if __name__ == "__main__":
    start_page = StartPage()
    start_page.mainloop()
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
