import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

import matplotlib.pyplot as plt

class GraphingCalculatorUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Graphing Calculator")

        self.equation_label = ttk.Label(root, text="Enter Equation (in terms of x):")
        self.equation_label.pack(pady=5)

        self.equation_entry = ttk.Entry(root, width=50)
        self.equation_entry.pack(pady=5)

        self.plot_button = ttk.Button(root, text="Plot", command=self.plot_graph)
        self.plot_button.pack(pady=5)

        self.figure = plt.Figure(figsize=(6, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, root)
        self.canvas.get_tk_widget().pack(pady=20)

    def plot_graph(self):
        equation = self.equation_entry.get()
        x = np.linspace(-10, 10, 400)
        try:
            y = eval(equation)
            self.ax.clear()
            self.ax.plot(x, y)
            self.ax.set_title(f"Graph of {equation}")
            self.canvas.draw()
        except Exception as e:
            tk.messagebox.showerror("Error", f"Invalid equation: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphingCalculatorUI(root)
    root.mainloop()