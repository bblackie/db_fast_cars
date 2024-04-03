import sqlite3

DATABASE = 'fast_cars.db'

def print_all_cars():

    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM car;"
        cursor.execute(sql)
        results = cursor.fetchall()

        for car in results:
            print(f"Car: {car[1]}")

if __name__ == "__main__":
    print_all_cars()
