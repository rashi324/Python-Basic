#Inheritance Class Polymorphism

# the child classes inherits the Vehicle methods

# Create a class called Vehicle and make
# Car, Boat, Plane child classes of Vehicle ?

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move")

class Car(Vehicle):
    pass

class Boat(Vehicle):

    def move(self):
        print("sail!")


class Plane(Vehicle):

    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang")  # create a car class
boat1 = Boat("ibiza", "Touring 20")  # create a boat class
plane1 = Plane("Boeing", "747")  # create a plane class

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()

    # Child classes inherits the properties and methods from the parent class.

    # In the example above you can see that the Car class is empty,
    # but it inherits brand, model, and move() from Vehicle.

    # The Boat and Plane classes also inherit brand, model, and move() from Vehicle,
    # but they both override the move() method.

    # Because of polymorphism we can execute the same method for all classes.