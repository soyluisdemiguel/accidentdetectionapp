import sqlite3
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from .config import db_path

router = APIRouter()

class User(BaseModel):
    username: str
    email: str
    notification_preferences: dict

class UserInDB(User):
    password: str

user_management = UserManagement(db_path)

@router.post("/users")
async def create_user(user: UserInDB):
    user_added = user_management.add_user(user.username, user.password, user.email, user.notification_preferences)
    if user_added:
        return {"message": "User created"}
    else:
        raise HTTPException(status_code=400, detail="User already exists")

@router.get("/users/{username}")
async def get_user(username: str):
    user = user_management.get_user(username)
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")

class UserManagement:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = sqlite3.connect(self.db_path)
        self.create_users_table()

    def create_users_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT UNIQUE,
            admin BOOLEAN DEFAULT 0
        )
        """
        self.connection.execute(query)
        self.connection.commit()

    def add_user(self, username, password, email, phone, admin=False):
        query = "INSERT INTO users (username, password, email, phone, admin) VALUES (?, ?, ?, ?, ?)"
        try:
            self.connection.execute(query, (username, password, email, phone, admin))
            self.connection.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def remove_user(self, username):
        query = "DELETE FROM users WHERE username = ?"
        self.connection.execute(query, (username,))
        self.connection.commit()

    def get_user(self, username):
        query = "SELECT * FROM users WHERE username = ?"
        result = self.connection.execute(query, (username,)).fetchone()
        if result:
            return {
                "id": result[0],
                "username": result[1],
                "password": result[2],
                "email": result[3],
                "phone": result[4],
                "admin": bool(result[5])
            }
        else:
            return None

    def get_users(self):
        query = "SELECT * FROM users"
        results = self.connection.execute(query).fetchall()
        users = []
        for row in results:
            users.append({
                "id": row[0],
                "username": row[1],
                "password": row[2],
                "email": row[3],
                "phone": row[4],
                "admin": bool(row[5])
            })
        return users

    def close(self):
        self.connection.close()


if __name__ == "__main__":
    user_management = UserManagement("user_management.db")
    user_management.add_user("johndoe", "password", "john@example.com", "555-1234", True)
    users = user_management.get_users()
    print(users)
    user_management.close()
