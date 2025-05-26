import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from lib.models.magazine import Magazine

def test_magazine_creation():
    mag = Magazine(name="Science Weekly", category="Science")
    mag.save()
    assert mag.id is not None

def test_magazine_articles_and_contributors_empty():
    mag = Magazine(name="EmptyMag", category="None")
    mag.save()
    assert mag.articles() == []
    assert mag.contributors() == []
