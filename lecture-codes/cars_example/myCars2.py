from ex_car import Car

# Three objects created from the class Car in 
# file myCarClassFile.py
c1 = Car("Skoda","Scout","2013")
c2 = Car("VW","Passat","1998")
c3 = Car("Volvo","V70","2007")

#print(c2.getMake())

# A list is created and car-objects are 
# stored in it (temporary stored - cleared after program ends)
myCars = [c1,c2,c3]

# for loop to step through
# the list with all cars
for c in myCars:
   print(c.get_make())
   print(c.get_year())
   
   # passing just the reference (c) to call the 
   # __str__ method automatically 
   # in the car class file
   print(c)
   

   
   