#Add Methods
#Add a method called welcome to the Student class ?

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):  # Child class
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):  # Corrected indentation here
        print("Welcome", self.firstname, self.lastname,
              "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2020)
x.welcome()

#If you add a method in the child class with the same name
# as a function in the parent class,
# the inheritance of the parent method will be overridden.