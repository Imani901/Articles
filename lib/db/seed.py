from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def seed():
    a1 = Author("Alice")
    a2 = Author("Bob")
    a1.save()
    a2.save()

    m1 = Magazine("Tech World", "Technology")
    m2 = Magazine("Nature Now", "Science")
    m1.save()
    m2.save()

    Article("AI for All", a1.id, m1.id).save()
    Article("Quantum Realms", a2.id, m2.id).save()
    Article("Green Earth", a1.id, m2.id).save()
    Article("Big Data", a1.id, m1.id).save()
    Article("Neural Nets", a1.id, m1.id).save()

if __name__ == '__main__':
    seed()
    print("Seed data inserted.")
