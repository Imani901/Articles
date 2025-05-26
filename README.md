# 📰 Articles Code Challenge – Phase 3

This project models a simple publishing system using **Python** and **SQLite** with raw SQL (no ORM).

It tracks relationships between:

- **Authors** – can write multiple Articles  
- **Articles** – belong to one Author and one Magazine  
- **Magazines** – can publish many Articles

---

## 📁 Project Structure

code-challenge/
├── lib/
│ ├── models/ # Author, Article, Magazine classes
│ └── db/ # DB schema, connection, seed data
├── scripts/ # Setup & query scripts
├── tests/ # Pytest-based test suite
├── env/ # (Virtual environment - gitignored)
├── README.md
└── .gitignore

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

### 1. Create and activate a virtual environment

```bash
python3 -m venv env
source env/bin/activate       # Windows: env\Scripts\activate
2. Install dependencies
bash
Copy
Edit
pip install pytest
3. Set up the database
bash
Copy
Edit
python3 scripts/setup_db.py     # Creates tables from schema.sql
python3 lib/db/seed.py          # (Optional) Populates database with sample data
🧪 Running Tests
We use pytest to test the core functionality.

From the root directory, run:

bash
Copy
Edit
PYTHONPATH=. pytest
This runs all tests in the tests/ folder:

test_author.py

test_article.py

test_magazine.py

Each file tests SQL logic, relationships, and method correctness.

🧠 Features
✅ Author
.save()

.add_article(magazine, title)

.articles()

.magazines()

.topic_areas()

@classmethod find_by_name(name)

✅ Magazine
.save()

.articles()

.contributors()

.article_titles()

.contributing_authors()

✅ Article
.save()

@classmethod find_by_id(id)

@classmethod find_by_author(author_id)

@classmethod find_by_magazine(magazine_id)

✅ Global SQL Transaction
python
Copy
Edit
add_author_with_articles(author_name, articles_data)
Inserts an author and multiple articles in one atomic transaction with rollback on error.

▶️ Sample Manual Queries
You can also run scripts/run_queries.py to manually test relationships:

bash
Copy
Edit
PYTHONPATH=. python3 scripts/run_queries.py
📌 .gitignore
Make sure to include:

markdown
Copy
Edit
env/
__pycache__/
*.db
*.pyc
