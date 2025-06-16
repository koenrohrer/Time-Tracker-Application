import sqlite3
from datetime import datetime, timedelta
from typing import List, Tuple

class Database:
    def __init__(self, db_path='time_tracker.db'):
        self.db_path = db_path
        self._create_tables()

    def _create_tables(self):
        """Create the time_entries table if it doesn't exist."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS time_entries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT NOT NULL,
                    start_time TEXT NOT NULL,
                    end_time TEXT NOT NULL,
                    hours REAL NOT NULL
                )
            ''')

    def clear_database(self) -> None:
        """Delete all entries from the database."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('DELETE FROM time_entries')
            conn.commit()

    def add_time_entry(self, date: datetime, start_time: datetime, end_time: datetime) -> Tuple[int, float]:
        """Add a new time entry and return the entry ID and hours."""
        duration = end_time - start_time
        hours = duration.total_seconds() / 3600

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute('''
                INSERT INTO time_entries (date, start_time, end_time, hours)
                VALUES (?, ?, ?, ?)
            ''', (
                date.strftime('%Y-%m-%d'),
                start_time.strftime('%Y-%m-%d %H:%M'),
                end_time.strftime('%Y-%m-%d %H:%M'),
                hours
            ))
            conn.commit()
            return cursor.lastrowid, hours

    def get_all_entries(self) -> List[Tuple]:
        """Get all time entries ordered by date descending."""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute('''
                SELECT date, start_time, end_time, hours
                FROM time_entries
                ORDER BY date DESC, start_time DESC
            ''')
            return [dict(row) for row in cursor.fetchall()]

    def get_total_hours(self) -> float:
        """Get the total hours across all entries."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute('SELECT SUM(hours) FROM time_entries')
            return cursor.fetchone()[0] or 0.0

    def get_weekly_total(self) -> float:
        """Get the total hours for the current week (Monday to Sunday)."""
        today = datetime.now()
        # Get the start of the week (Monday)
        start_of_week = today - timedelta(days=today.weekday())
        start_of_week = start_of_week.replace(hour=0, minute=0, second=0, microsecond=0)
        # Get the end of the week (Sunday)
        end_of_week = start_of_week + timedelta(days=6, hours=23, minutes=59, seconds=59)

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute('''
                SELECT SUM(hours) FROM time_entries 
                WHERE date BETWEEN ? AND ?
            ''', (
                start_of_week.strftime('%Y-%m-%d'),
                end_of_week.strftime('%Y-%m-%d')
            ))
            return cursor.fetchone()[0] or 0.0 