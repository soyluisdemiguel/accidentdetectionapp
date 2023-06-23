import sqlite3

class Feedback:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = sqlite3.connect(self.db_path)
        self.create_feedback_table()

    def create_feedback_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            feedback TEXT NOT NULL
        )
        """
        self.connection.execute(query)
        self.connection.commit()

    def add_feedback(self, username, feedback):
        query = "INSERT INTO feedback (username, feedback) VALUES (?, ?)"
        self.connection.execute(query, (username, feedback))
        self.connection.commit()

    def get_all_feedback(self):
        query = "SELECT * FROM feedback"
        results = self.connection.execute(query).fetchall()
        feedback_list = []
        for row in results:
            feedback_list.append({
                "id": row[0],
                "username": row[1],
                "feedback": row[2]
            })
        return feedback_list

    def close(self):
        self.connection.close()

if __name__ == "__main__":
    feedback_manager = Feedback("feedback.db")
    feedback_manager.add_feedback("john_doe", "Great app!")
    feedback_manager.add_feedback("jane_doe", "Could use some improvements.")
    print(feedback_manager.get_all_feedback())
    feedback_manager.close()
