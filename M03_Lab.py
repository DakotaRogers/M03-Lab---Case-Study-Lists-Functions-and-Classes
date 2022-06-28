# Dakota Rogers
# M03_Lab
# This program will list vehicle attributes in an easy to read format
# class vehicle with variable type to display if it is a car or a truck
# subclass automobile to display the variables: year, make, model, doors, and roof type
#  super class named vehicle
class vehicle():
    # attribute of type
    def __init__(self, type):
        self.type = type

# class called automobile that inherits attribute from vehicle


class automobile(vehicle):
    # contain yaer, make, model, doors(2 or 4), roof(solid or sun roof).
    def __init__(self, year, make, model, doors, roof):
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof


# accept user input for the attributes
type = input("Is the vehicle a truck or a car? ")
year = input("What year is the vehicle? ")
make = input("What make is the vehicle? ")
model = input("What model is the vehicle? ")
doors = input("How many doors does the vehicle have? ")
roof = input("Does it have a sun-roof or a solid roof? ")

# output data in an easy-to-read format
print("\nVehicle Type: "+type)
print("\nYear: "+year)
print("\nMake: "+make)
print("\nModel: "+model)
print("\nNumber of doors: "+doors)
print("\nType of roof: "+roof)
