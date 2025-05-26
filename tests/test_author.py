import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from lib.models.author import Author

def test_author_can_be_created_and_saved():
    author = Author("Test Author")
    author.save()

    assert author.id is not None

def test_author_can_be_found_by_id():
    author = Author("Find Me")
    author.save()

    found = Author.find_by_id(author.id)
    assert found.name == "Find Me"
