class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.add_button.config(command=self.add)
        self.view.subtract_button.config(command=self.subtract)
        self.view.multiply_button.config(command=self.multiply)
        self.view.divide_button.config(command=self.divide)

    def add(self):
        num1 = int(self.view.num1_entry.get())
        num2 = int(self.view.num2_entry.get())
        self.model.set_numbers(num1, num2)
        result = self.model.add()
        self.view.result_label.configure(text="Résultat: " + str(result))

    def subtract(self):
        num1 = int(self.view.num1_entry.get())
        num2 = int(self.view.num2_entry.get())
        self.model.set_numbers(num1, num2)
        result = self.model.subtract()
        self.view.result_label.configure(text="Résultat: " + str(result))

    def multiply(self):
        num1 = int(self.view.num1_entry.get())
        num2 = int(self.view.num2_entry.get())
        self.model.set_numbers(num1, num2)
        result = self.model.multiply()
        self.view.result_label.configure(text="Résultat: " + str(result))

    def divide(self):
        num1 = int(self.view.num1_entry.get())
        num2 = int(self.view.num2_entry.get())
        self.model.set_numbers(num1, num2)
        result = self.model.divide()
        self.view.result_label.configure(text="Résultat: " + str(result))