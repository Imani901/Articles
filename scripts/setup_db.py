# scripts/setup_db.py
import sqlite3

def setup_db():
    conn = sqlite3.connect('articles.db')
    cursor = conn.cursor()
    
    with open('lib/db/schema.sql') as f:
        cursor.executescript(f.read())

    conn.commit()
    conn.close()

if __name__ == '__main__':
    setup_db()
    print("Database setup complete.")
