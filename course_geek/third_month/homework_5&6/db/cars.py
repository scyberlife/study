import sqlite3
from pathlib import Path

def db_ini():
    MAIN_PATH = Path(__file__).parent.parent
    DB_NAME = 'cars.sqlite'
    global db, cur
    db = sqlite3.connect(MAIN_PATH / DB_NAME)
    cur = db.cursor()
    print("Create BD Cars")


def create_tab():
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS cars(
        model TEXT,
        price TEXT,
        mileage INTEGER,
        info TEXT
        )
        """
    )
    db.commit()


def done_cars():
    cur.execute(
        """
        SELECT * FROM  cars
        """
    )
    return cur.fetchall()


def get_cars(cars):
    db_ini()
    create_tab()
    cur.executemany("""INSERT INTO cars (
    model,
    price,
    mileage,
    info) VALUES (?, ?, ?, ?)""", cars)
    db.commit()


if __name__ == "__main__":
    db_ini()
    create_tab()
    done_cars()