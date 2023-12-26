import pyodbc

class Database:
    def __init__(self):
        self.conn = pyodbc.connect(
            'DRIVER={SQL Server};'
            'SERVER=ISAACINOU;'
            'DATABASE=TEST_PYTHON;'
            'Trusted_Connection=yes;'
        )
        self.cursor = self.conn.cursor()

    def fetch_all_records(self):
        self.cursor.execute("SELECT * FROM Recette")
        return self.cursor.fetchall()

    def insert_record(self, data):
        self.cursor.execute("INSERT INTO Recette (column1, column2, column3) VALUES (?, ?, ?)",
                            data['column1'], data['column2'], data['column3'])
        self.conn.commit()

    def update_record(self, data):
        self.cursor.execute("UPDATE Recette SET column1=?, column2=?, column3=? WHERE id=?",
                            data['column1'], data['column2'], data['column3'], data['id'])
        self.conn.commit()

    def delete_record(self, record_id):
        self.cursor.execute("DELETE FROM Recette WHERE id_recette=?", record_id)
        self.conn.commit()