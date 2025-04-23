#Class Polymorphism

#Polymorphism is often used in Class methods,
# where we can have multiple classes with the same method name.

#Different classes with the same method ?

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")


class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.type = type

    def move(self):
        print("Sail!")


class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Flt!")

car1 = Car ("Ford","Mustang" )  #create a car class
boat1 = Boat ("ibiza", "Touring 20") #create a boat class
plane1 = Plane ("Boeing", "747") #create a plane class

for x in (car1, boat1, plane1):
    x.move()