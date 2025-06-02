from lib.db.connection import get_connection

all = []

class Magazine:
    def __init__(self, name, category, id=None):
        self.id = id
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @classmethod
    def find_by_category(cls, category):
        return [m for m in cls.all if m.category == category]

    @classmethod
    def with_multiple_authors(cls):
        return [m for m in cls.all if len(set(a.author for a in m.articles())) > 1]

    @classmethod
    def article_counts(cls):
        return {m: len(m.articles()) for m in cls.all}

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (self.name, self.category))
            self.id = cursor.lastrowid
        else:
            cursor.execute("UPDATE magazines SET name = ?, category = ? WHERE id = ?", (self.name, self.category, self.id))
        conn.commit()
        conn.close()

    def articles(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE magazine_id = ?", (self.id,))
        results = cursor.fetchall()
        conn.close()
        return results

    def contributors(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT a.* FROM authors a
            JOIN articles ar ON ar.author_id = a.id
            WHERE ar.magazine_id = ?
        """, (self.id,))
        results = cursor.fetchall()
        conn.close()
        return results

    def article_titles(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT title FROM articles WHERE magazine_id = ?", (self.id,))
        results = [row['title'] for row in cursor.fetchall()]
        conn.close()
        return results

    def contributing_authors(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT a.*, COUNT(ar.id) as article_count FROM authors a
            JOIN articles ar ON a.id = ar.author_id
            WHERE ar.magazine_id = ?
            GROUP BY a.id
            HAVING COUNT(ar.id) > 2
        """, (self.id,))
        results = cursor.fetchall()
        conn.close()
        return results
