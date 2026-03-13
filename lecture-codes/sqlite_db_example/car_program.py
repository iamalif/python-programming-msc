import sqlite3
from car import Car

# Three objects created from the class Car in 
# file myCarClassFile.py
c1 = Car("Skoda","Scout","2015")
c2 = Car("Volvo","V70","2007")

# A list is created and car-objects are 
# stored in it (temporary stored - cleared after program ends)
myCars = [c1,c2]
myCars.append(Car("Ford","GT","1985"))
myCars.append(Car("BMW","GT","1990"))
myCars.append(Car("Mercedes","GT","2010"))

mk = input("Whats the make?")
md = input("Whats the model?")
yr = input("Whats the year?")

myCars.append(Car(mk,md,yr))

#============== GO THROUGH LIST OF CARS AND STORE IN DB ==============================================================================

conn = sqlite3.connect('my_cars.db')
#print "Opened database successfully";

for c in myCars:
   #print(c)
   # execute statements each iteration in for loop
   # INSERT INTO cars (make,model,year) VALUES (?, ?, ?), (c.get_make(),c.get_model(),c.get_year())
   conn.execute("INSERT INTO cars (make,model,year) VALUES (?, ?, ?)",(c.get_make(),c.get_model(),c.get_year()))

conn.commit()
#print("Records created successfully")
conn.close()

#============== READ FROM DB ==============================================================================

conn = sqlite3.connect('my_cars.db')
#print "Opened database successfully";

cursor = conn.execute("SELECT id, make, model, year FROM cars")
for row in cursor:
   print("ID = ", row[0])
   print("MAKE = ", row[1])
   print("MODEL = ", row[2])
   print("YEAR = ", row[3], "\n")

conn.close()
