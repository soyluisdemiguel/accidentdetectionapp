import sqlite3
import geopy.distance
from .config import db_path

class Geolocation:
    def __init__(self):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        query_events = """
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            latitude REAL NOT NULL,
            longitude REAL NOT NULL
        )
        """
        query_emergency_teams = """
        CREATE TABLE IF NOT EXISTS emergency_teams (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            latitude REAL NOT NULL,
            longitude REAL NOT NULL
        )
        """
        self.cursor.execute(query_events)
        self.cursor.execute(query_emergency_teams)
        self.conn.commit()

    def add_event(self, event):
        self.cursor.execute(
            "INSERT INTO events (latitude, longitude) VALUES (?, ?)",
            (event["latitude"], event["longitude"]),
        )
        self.conn.commit()

    def add_emergency_team(self, team):
        self.cursor.execute(
            "INSERT INTO emergency_teams (latitude, longitude) VALUES (?, ?)",
            (team["latitude"], team["longitude"]),
        )
        self.conn.commit()

    def find_nearest_emergency_team(self, event_location):
        self.cursor.execute("SELECT * FROM emergency_teams")
        emergency_teams = self.cursor.fetchall()
        nearest_team = None
        min_distance = float("inf")

        for team in emergency_teams:
            team_location = (team[1], team[2])
            distance = geopy.distance.distance(event_location, team_location).m
            if distance < min_distance:
                min_distance = distance
                nearest_team = {
                    "id": team[0],
                    "latitude": team[1],
                    "longitude": team[2]
                }

        return nearest_team, min_distance

    def update_emergency_team_location(self, team_id, new_location):
        self.cursor.execute(
            "UPDATE emergency_teams SET latitude = ?, longitude = ? WHERE id = ?",
            (new_location[0], new_location[1], team_id),
        )
        self.conn.commit()

    def close(self):
        self.conn.close()
