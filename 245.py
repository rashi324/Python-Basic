#Add Properties
#Add a property called graduationyear to the Student class ?

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):  # Moved outside and fixed indentation
    def __init__(self, fname, lname):
        super().__init__(fname, lname)  # Capital 'P'
        self.graduationyear = 2020

x = Student("Mike", "Olsen")
print(x.graduationyear)