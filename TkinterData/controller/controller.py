from model.model import Database
from view.view import ApplicationView

class ApplicationController:
    def __init__(self):
        self.model = Database()
        self.view = ApplicationView(self)

    def fetch_all_records(self):
        return self.model.fetch_all_records()

    def create_record(self, data):
        self.model.insert_record(data)

    def update_record(self, data):
        self.model.update_record(data)

    def delete_record(self, record_id):
        self.model.delete_record(record_id)

