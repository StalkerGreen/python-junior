import sqlite3


class Database:
    def __init__(self, db_name="test.db"):
        self.conn = sqlite3.connect(db_name)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def get_all_notes(self):
        self.cursor.execute("SELECT * FROM notes")
        return self.cursor.fetchall()

    def add_note(self, text, created_at):
        self.cursor.execute(
            "INSERT INTO notes (text, created_at) VALUES (?, ?)",
            (text, created_at)
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def delete_note(self, note_id):
        self.cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
        self.conn.commit()
        return self.cursor.rowcount

    def close(self):
        self.cursor.close()

