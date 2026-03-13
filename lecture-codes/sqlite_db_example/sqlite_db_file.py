import sqlite3

conn = sqlite3.connect('my_cars.db')

print("Opened database successfully");

connString = '''CREATE TABLE IF NOT EXISTS cars
         (id INTEGER PRIMARY KEY NOT NULL,
         make TEXT NOT NULL,
         model TEXT NOT NULL,
         year TEXT);'''

conn.execute(connString)
print("Table created successfully")

conn.execute("INSERT INTO cars (id,make,model,year) VALUES (1, 'Opel', 'Ascona', '1985');")
conn.execute("INSERT INTO cars (id,make,model,year) VALUES (2, 'Kia', 'Sorento', '2005');")
conn.execute("INSERT INTO cars (id,make,model,year) VALUES (3, 'Dodge', 'Truck', '1999');")

conn.commit()
print("Records created successfully")

conn.close()
