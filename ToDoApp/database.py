import sqlite3 as sql

class TaskDatabase:
    def __init__(self, db_name='listOfTasks.db'):
        # Connect to the SQLite database file
        self.conn = sql.connect(db_name)
        self.cursor = self.conn.cursor()
        
        # Create the tasks table if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                title TEXT,
                completed INTEGER,
                reminder TEXT
            )
        ''')
        self.conn.commit()

    def add_task(self, title, reminder=None):
        self.cursor.execute('INSERT INTO tasks (title, completed, reminder) VALUES (?, ?, ?)', (title, 0, reminder))
        self.conn.commit()

    def delete_task(self, title):
        self.cursor.execute('DELETE FROM tasks WHERE title = ?', (title,))
        self.conn.commit()

    def delete_all(self):
        self.cursor.execute('DELETE FROM tasks')
        self.conn.commit()

    def get_tasks(self):
        self.cursor.execute('SELECT title, completed, reminder FROM tasks')
        return self.cursor.fetchall()

    def mark_complete(self, title):
        self.cursor.execute('UPDATE tasks SET completed = 1 WHERE title = ?', (title,))
        self.conn.commit()

    def close(self):
        self.conn.close()
