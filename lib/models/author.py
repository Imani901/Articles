from lib.db.connection import get_connection

all = []

class Author:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name
        Author.all.append(self)


    @classmethod
    def find_by_name(cls, name):
        for author in cls.all:
            if author.name == name:
                return author
        return None

    @classmethod
    def top_author(cls):
        return max(cls.all, key=lambda a: len(a.articles()), default=None)    

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()

        if self.id is None:
            cursor.execute("INSERT INTO authors (name) VALUES (?)", (self.name,))
            self.id = cursor.lastrowid
        else:
            cursor.execute("UPDATE authors SET name = ? WHERE id = ?", (self.name, self.id))

        conn.commit()
        conn.close()

    @classmethod
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return cls(name=row['name'], id=row['id'])

    def articles(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE author_id = ?", (self.id,))
        results = cursor.fetchall()
        conn.close()
        return results

    def magazines(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT m.* FROM magazines m
            JOIN articles a ON a.magazine_id = m.id
            WHERE a.author_id = ?
        """, (self.id,))
        results = cursor.fetchall()
        conn.close()
        return results

    def add_article(self, magazine, title):
        from lib.models.article import Article
        article = Article(title=title, author_id=self.id, magazine_id=magazine.id)
        article.save()
        return article
    
    def topic_areas(self):
     """
     Returns a list of unique  magazine categories this author has contributed to.
     """
     conn = get_connection()
     cursor = conn.cursor()
     cursor.execute("""
         SELECT DISTINCT m.category FROM magazines m
         JOIN articles a ON m.id = a.magazine_id
         WHERE a.author_id = ?
     """, (self.id,))
     results = [row['category'] for row in cursor.fetchall()]
     conn.close()
     return results
