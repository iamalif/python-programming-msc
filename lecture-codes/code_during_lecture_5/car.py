
class Car:

    def __init__(self, make):
        self.__make = make

    def get_make(self):
        return self.__make

    def set_make(self, mke):
        self.__make = mke

 
    def __str__(self):
        return "The make is: " + self.__make




