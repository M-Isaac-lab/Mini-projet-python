import tkinter as tk
from tkinter import messagebox

class ApplicationView:
    def __init__(self, controller):
        self.controller = controller

        self.root = tk.Tk()
        self.root.title("CRUD App")

        self.entry_column1 = tk.Entry(self.root)
        self.entry_column1.pack()

        self.entry_column2 = tk.Entry(self.root)
        self.entry_column2.pack()

        self.entry_column3 = tk.Entry(self.root)
        self.entry_column3.pack()

        self.button_create = tk.Button(self.root, text="Create", command=self.create_record)
        self.button_create.pack()

        self.button_update = tk.Button(self.root, text="Update", command=self.update_record)
        self.button_update.pack()

        self.button_delete = tk.Button(self.root, text="Delete", command=self.delete_record)
        self.button_delete.pack()

        self.listbox = tk.Listbox(self.root)
        self.listbox.pack()

        self.load_records()

        self.root.mainloop()

    def load_records(self):
        self.listbox.delete(0, tk.END)
        records = self.controller.fetch_all_records()
        for record in records:
            self.listbox.insert(tk.END, record)

    def create_record(self):
        data = {
            'column1': self.entry_column1.get(),
            'column2': self.entry_column2.get(),
            'column3': self.entry_column3.get()
        }
        self.controller.create_record(data)
        self.load_records()

    def update_record(self):
        selected_record = self.listbox.curselection()
        if selected_record:
            record_id = self.listbox.get(selected_record)[0]
            data = {
                'id': record_id,
                'column1': self.entry_column1.get(),
                'column2': self.entry_column2.get(),
                'column3': self.entry_column3.get()
            }
            self.controller.update_record(data)
            self.load_records()
        else:
            messagebox.showwarning("No Record Selected", "Please select a record to update.")

    def delete_record(self):
        selected_record = self.listbox.curselection()
        if selected_record:
            record_id = self.listbox.get(selected_record)[0]
            self.controller.delete_record(record_id)
            self.load_records()
        else:
            messagebox.showwarning("No Record Selected", "Please select a record to delete.")