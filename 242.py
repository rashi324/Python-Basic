# Python Inheritance

# Inheritance allows us to define a class that inherits all the methods
# and properties from another class.

# Parent class is the class being inherited from, also called base class.

# Child class is the class that inherits from another class,
# also called derived class.

# Create a Parent Class

# Create a class named Person,
# with firstname and lastname properties, and a printname method:

class Person:
    def __init__(self, fname, lname):  # Fixed: comma instead of period
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# Use the person class to create an object,
# and then execute the printname method:

x = Person("rashi", "gill")
x.printname()


#Create a Child Class

#To create a class that inherits the functionality from another class,
# send the parent class as a parameter when creating the child class:


#Create a class named Student,
# which will inherit the properties and methods from the Person class:

class Student(Person):
    pass

#Note: Use the pass keyword when you do not want to add any other properties
# or methods to the class.

#Now the Student class has the same properties and methods as the Person class.

#Use the Student class to create an object,
# and then execute the printname method:

x = Student("ayra", "rashi")
x.printname()