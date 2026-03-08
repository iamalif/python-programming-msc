
from car import Car as c

car = c("Volvo")
car2 = c("Mercedes")
 
cars = [car, car2]
print(cars[1].get_make())

print(car.get_make())
        
car.set_make("BMW")
print(car.get_make())

print(car2.get_make())

print(car)

