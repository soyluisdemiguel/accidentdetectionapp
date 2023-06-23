import sqlite3
import geopy.distance
from .config import db_path

class ProximityAlerts:
    def __init__(self):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_alerts_table()

    def create_alerts_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS proximity_alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            latitude REAL NOT NULL,
            longitude REAL NOT NULL,
            radius REAL NOT NULL
        )
        """
        self.cursor.execute(query)
        self.conn.commit()

    def add_alert(self, alert):
        self.cursor.execute(
            "INSERT INTO proximity_alerts (latitude, longitude, radius) VALUES (?, ?, ?)",
            (alert["latitude"], alert["longitude"], alert["radius"]),
        )
        self.conn.commit()

    def check_proximity(self, user_location):
        self.cursor.execute("SELECT * FROM proximity_alerts")
        alerts = self.cursor.fetchall()
        triggered_alerts = []

        for alert in alerts:
            alert_location = (alert[1], alert[2])
            distance = geopy.distance.distance(user_location, alert_location).m
            if distance <= alert[3]:
                triggered_alerts.append({
                    "id": alert[0],
                    "latitude": alert[1],
                    "longitude": alert[2],
                    "radius": alert[3]
                })

        return triggered_alerts

    def close(self):
        self.conn.close()
