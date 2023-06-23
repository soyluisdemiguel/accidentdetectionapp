import sqlite3
from .config import db_path

class AdminManagement:
    def __init__(self):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_admins_table()

    def create_admins_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS admins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT UNIQUE NOT NULL
        )
        """
        self.cursor.execute(query)
        self.conn.commit()

    def add_admin(self, name, email, phone):
        self.cursor.execute(
            "INSERT INTO admins (name, email, phone) VALUES (?, ?, ?)",
            (name, email, phone),
        )
        self.conn.commit()

    def remove_admin(self, admin_id):
        self.cursor.execute("DELETE FROM admins WHERE id = ?", (admin_id,))
        self.conn.commit()

    def list_admins(self):
        self.cursor.execute("SELECT * FROM admins")
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
