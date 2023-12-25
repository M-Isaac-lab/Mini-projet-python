import tkinter as tk
from model.model import Model
from view.view import View
from controller.controller import Controller

if __name__ == "__main__":
    root = tk.Tk()
    model = Model()
    view = View(root)
    controller = Controller(model, view)
    root.mainloop()