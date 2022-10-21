import os
import sqlite3

db_filename = "sakila.db"


def get_actors():
    if not os.path.exists(db_filename):
        print("Need to create new schema.")
    else:
        print("Database exists, assume schema does too.")
        with sqlite3.connect(db_filename) as conn:
            cursor = conn.cursor()
            result = cursor.execute("SELECT * FROM actor;")
            # print(result.fetchone())
            actors = result.fetchall()
            # print(actors)
            return actors


if __name__ == "__main__":
    get_actors()
