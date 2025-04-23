#Add a year parameter,
# and pass the correct year when creating objects ?

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):  # Moved outside and fixed indentation
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)  # Capital 'P'
        self.graduationyear = year

x = Student("Mike", "Olsen" , 2020)
print(x.graduationyear)