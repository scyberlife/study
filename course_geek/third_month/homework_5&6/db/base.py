import sqlite3
from pathlib import Path


def db_init():
    PROJECT_DIR = Path(__file__).parent.parent
    DB_FILE = 'db.sqlite'
    global  db, cur
    db = sqlite3.connect(PROJECT_DIR/DB_FILE)
    cur = db.cursor()
    print("create BD")

def create_tables():
    cur.execute("""CREATE TABLE IF NOT EXISTS products(
        product_id INTEGER PRIMARY KEY,
        name TEXT,
        price INTEGER,
        photo TEXT
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS orders(
        order_id INTEGER PRIMARY KEY,
        user_name TEXT,
        address TEXT,
        product_id INTEGER,
        FOREIGN KEY (product_id)
            REFERENCES  products (product_id)
            ON DELETE CASCADE
         
    )""")
    db.commit()

def delete_tables():
    cur.execute("""DROP TABLE IF EXISTS products""")
    db.commit()

def populate_products():
    cur.execute("""INSERT INTO products (name, price, photo) VALUES
                            ('The Republic', 2.99, 'images/the_republic.jpg'),
                            ('The theory of everything', 2.85, 'images/the_theory_of_everything.jpg'),
                            ('The enigma', 4.99, 'images/the_enigma.jpg'),
                            ('Guide to the Galaxy', 3.85, 'images/guide_to_the_Galaxy.jpg'),
                            ('The Emotion Machine', 5.10, 'images/the_emotion_machine.jpg')
    """)
    db.commit()


def get_products():
    cur.execute("""SELECT * FROM products""")
    all_products = cur.fetchall()
    return all_products


if __name__ == "__main__":
    db_init()
    delete_tables()
    create_tables()
    populate_products()
    get_products()