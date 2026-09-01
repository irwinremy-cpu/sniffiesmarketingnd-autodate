"""
Database module for storing user data and interaction history.
"""

import sqlite3
import os
from typing import List, Dict, Any
from datetime import datetime
from utils import log_message


class DatabaseManager:
    """Manages SQLite database for storing user data and interactions."""
    
    def __init__(self, db_path: str = "data/sniffies.db"):
        self.db_path = db_path
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.init_database()
        
    def init_database(self):
        """Initialize the database with required tables."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Create users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT,
                age INTEGER,
                location TEXT,
                interests TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Create interactions table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS interactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                action_type TEXT,
                target_user TEXT,
                message TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        conn.commit()
        conn.close()
        log_message("Database initialized")
        
    def save_user(self, username: str, email: str = None, age: int = None, 
                  location: str = None, interests: List[str] = None) -> int:
        """Save a user to the database."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        interests_str = ",".join(interests) if interests else ""
        
        try:
            cursor.execute('''
                INSERT OR REPLACE INTO users 
                (username, email, age, location, interests, updated_at)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (username, email, age, location, interests_str, datetime.now()))
            
            user_id = cursor.lastrowid
            conn.commit()
            log_message(f"Saved user: {username}")
            return user_id
        except Exception as e:
            log_message(f"Error saving user {username}: {str(e)}")
            return None
        finally:
            conn.close()
            
    def get_user(self, username: str) -> Dict[str, Any]:
        """Retrieve a user from the database."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return {
                'id': row[0],
                'username': row[1],
                'email': row[2],
                'age': row[3],
                'location': row[4],
                'interests': row[5].split(',') if row[5] else [],
                'created_at': row[6],
                'updated_at': row[7]
            }
        return None
        
    def save_interaction(self, user_id: int, action_type: str, target_user: str = None, 
                        message: str = None):
        """Save an interaction to the database."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                INSERT INTO interactions 
                (user_id, action_type, target_user, message)
                VALUES (?, ?, ?, ?)
            ''', (user_id, action_type, target_user, message))
            
            conn.commit()
            log_message(f"Saved interaction for user {user_id}")
        except Exception as e:
            log_message(f"Error saving interaction: {str(e)}")
        finally:
            conn.close()
            
    def get_user_interactions(self, user_id: int) -> List[Dict[str, Any]]:
        """Retrieve interactions for a specific user."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM interactions 
            WHERE user_id = ? 
            ORDER BY timestamp DESC
        ''', (user_id,))
        
        rows = cursor.fetchall()
        conn.close()
        
        return [
            {
                'id': row[0],
                'user_id': row[1],
                'action_type': row[2],
                'target_user': row[3],
                'message': row[4],
                'timestamp': row[5]
            }
            for row in rows
        ]
        
    def save_advertisement(self, title: str, description: str, target_audience: str):
        """Save an advertisement to the database."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                INSERT INTO advertisements (title, description, target_audience)
                VALUES (?, ?, ?)
            ''', (title, description, target_audience))
            
            conn.commit()
            log_message(f"Saved advertisement: {title}")
        except Exception as e:
            log_message(f"Error saving advertisement {title}: {str(e)}")
        finally:
            conn.close()
            
    def get_all_advertisements(self) -> List[Dict[str, Any]]:
        """Retrieve all advertisements."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM advertisements ORDER BY created_at DESC')
        rows = cursor.fetchall()
        conn.close()
        
        return [
            {
                'id': row[0],
                'title': row[1],
                'description': row[2],
                'target_audience': row[3],
                'created_at': row[4]
            }
            for row in rows
        ]