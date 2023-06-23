import sqlite3
from fastapi import APIRouter, WebSocket
from datetime import datetime

router = APIRouter()

class NotificationSystem:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = sqlite3.connect(self.db_path)
        self.create_notifications_table()

    def create_notifications_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS notifications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            message TEXT NOT NULL,
            sent_at DATETIME NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
        """
        self.connection.execute(query)
        self.connection.commit()

    def add_notification(self, user_id, message):
        query = "INSERT INTO notifications (user_id, message, sent_at) VALUES (?, ?, ?)"
        sent_at = datetime.now()
        self.connection.execute(query, (user_id, message, sent_at))
        self.connection.commit()

    def get_notifications(self, user_id):
        query = "SELECT * FROM notifications WHERE user_id = ?"
        results = self.connection.execute(query, (user_id,)).fetchall()
        notifications = []
        for row in results:
            notifications.append({
                "id": row[0],
                "user_id": row[1],
                "message": row[2],
                "sent_at": row[3]
            })
        return notifications

    def delete_notification(self, notification_id):
        query = "DELETE FROM notifications WHERE id = ?"
        self.connection.execute(query, (notification_id,))
        self.connection.commit()

    def close(self):
        self.connection.close()

@router.websocket("/ws/notifications")
async def websocket_notifications(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            data = await websocket.receive_text()
            await websocket.send_text(f"Received: {data}")
        except Exception as e:
            await websocket.close()
            break

if __name__ == "__main__":
    notification_system = NotificationSystem("notification_system.db")
    notification_system.add_notification(1, "An accident has been detected.")
    notifications = notification_system.get_notifications(1)
    print(notifications)
    notification_system.close()
