import sqlite3

db = sqlite3.connect('fast_cars.db')
cursor = db.cursor()
sql = "SELECT * FROM car;"
cursor.execute(sql)
results = cursor.fetchall()

for car in results:
    print(f"Car: {car[1]}")
