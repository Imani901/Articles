from lib.db.connection import get_connection

all = []

class Article:
    def __init__(self, title, author_id, magazine_id, id=None):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.magazine_id = magazine_id
        Article.all.append(self)

    @classmethod
    def find_by_title(cls, title):
        for article in cls.all:
            if article.title == title:
                return article
        return None

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", 
                           (self.title, self.author_id, self.magazine_id))
            self.id = cursor.lastrowid
        else:
            cursor.execute("UPDATE articles SET title = ?, author_id = ?, magazine_id = ? WHERE id = ?", 
                           (self.title, self.author_id, self.magazine_id, self.id))
        conn.commit()
        conn.close()

    @classmethod
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(title=row["title"], author_id=row["author_id"], magazine_id=row["magazine_id"], id=row["id"])


from lib.db.connection import get_connection

def add_author_with_articles(author_name, articles_data):
    """
    Adds a new author and multiple articles in a single transaction.
    articles_data: list of dicts like {'title': ..., 'magazine_id': ...}
    """
    conn = get_connection()
    try:
        conn.execute("BEGIN TRANSACTION")
        cursor = conn.cursor()

        # Insert new author
        cursor.execute(
            "INSERT INTO authors (name) VALUES (?)",
            (author_name,)
        )
        author_id = cursor.lastrowid

        # Insert each article
        for article in articles_data:
            cursor.execute(
                "INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
                (article['title'], author_id, article['magazine_id'])
            )

        conn.commit()
        return True
    except Exception as e:
        conn.rollback()
        print(f"Transaction failed: {e}")
        return False
    finally:
        conn.close()
