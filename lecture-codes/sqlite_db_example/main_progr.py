import sqlite3

conn = sqlite3.connect('my_cars.db')
#print "Opened database successfully";

cursor = conn.execute("SELECT id, make, model, year from cars")
for row in cursor:
   print("ID = ", row[0])
   print("MAKE = ", row[1])
   print("MODEL = ", row[2])
   print("YEAR = ", row[3], "\n")

#print("Operation done successfully")






