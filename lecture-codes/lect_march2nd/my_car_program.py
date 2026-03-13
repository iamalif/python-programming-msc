from car_class import Car

# Three objects are created from the class Car in file car.py
c1 = Car("Skoda", "Scout", "2013")
c2 = Car("VW", "Passat", "1998")
c3 = Car("Volvo", "V70", "2007")

# A list is created and car-objects are 
# stored in it (temporary stored - cleared after program ends)
myCars = [c1, c2, c3]

# =========================================================================
# WRITING DATA, EACH OBJECT CREATED ABOVE, TO FILE IN
# THE FORM OF STRINGS! (TEXT)
# =========================================================================
# Open a file named my_cars.txt.
outfile = open("my_cars.txt", "w")

for car in myCars:
    c_txt = car.get_make() + "," + car.get_model() + "," + car.get_year()
    outfile.write(c_txt + "\n")

outfile.close()

# =========================================================================
# OPEN A FILE FOR READING WITH DATA, about cars, STORED FROM I.E. AN EARLIER SESSION
# =========================================================================

# Open a file named my_cars.txt.
infile = open("my_cars.txt", "r")

# get content from file, returned as a list ! so the
# car_temp_list will automatically be referencing a new list
# returned from the method readlines() of the file object "infile"
car_temp_list = infile.readlines()

infile.close()

#print(car_temp_list)

for each_position in car_temp_list:
    tmp_list = each_position.rsplit(',')  # ["Skoda","Scout","2013"]
    #print(tmp_list[0])
    tmp_car_obj = Car(tmp_list[0], tmp_list[1], tmp_list[2])
    # Simple way of adding new objects to 
    # the end of the list by using method append()
    myCars.append(tmp_car_obj)

#print(myCars[0],myCars[1])

# Just a print of the actual class variable
# holding the value of last id added 
# print(myCars[0].__class__.counter)


