import tkinter as tk

class View:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculatrice")

        self.num1_label = tk.Label(root, text="Nombre 1:")
        self.num1_label.grid(row=0, column=0, padx=10, pady=10)
        self.num1_entry = tk.Entry(root)
        self.num1_entry.grid(row=0, column=1, padx=10, pady=10)

        self.num2_label = tk.Label(root, text="Nombre 2:")
        self.num2_label.grid(row=1, column=0, padx=10, pady=10)
        self.num2_entry = tk.Entry(root)
        self.num2_entry.grid(row=1, column=1, padx=10, pady=10)

        self.add_button = tk.Button(root, text="Addition")
        self.add_button.grid(row=2, column=0, padx=10, pady=10)

        self.subtract_button = tk.Button(root, text="Soustraction")
        self.subtract_button.grid(row=2, column=1, padx=10, pady=10)

        self.multiply_button = tk.Button(root, text="Multiplication")
        self.multiply_button.grid(row=3, column=0, padx=10, pady=10)

        self.divide_button = tk.Button(root, text="Division")
        self.divide_button.grid(row=3, column=1, padx=10, pady=10)

        self.result_label = tk.Label(root, text="Résultat: ")
        self.result_label.grid(row=4, column=0, padx=10, pady=10)