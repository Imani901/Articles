from lib.db.connection import get_connection

def debug():
    conn = get_connection()
    cursor = conn.cursor()

    print("📄 AUTHORS")
    cursor.execute("SELECT * FROM authors")
    for row in cursor.fetchall():
        print(dict(row))

    print("\n📄 ARTICLES")
    cursor.execute("SELECT * FROM articles")
    for row in cursor.fetchall():
        print(dict(row))

    print("\n📄 MAGAZINES")
    cursor.execute("SELECT * FROM magazines")
    for row in cursor.fetchall():
        print(dict(row))

    conn.close()

if __name__ == '__main__':
    debug()
