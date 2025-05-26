import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def test_article_creation():
    author = Author("Writer")
    author.save()

    mag = Magazine("Mag1", "Tech")
    mag.save()

    article = Article(title="My First", author_id=author.id, magazine_id=mag.id)
    article.save()

    assert article.id is not None
