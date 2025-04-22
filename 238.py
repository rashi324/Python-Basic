#Modify Object Properties
#You can modify properties on objects like this

#  Set the age of p1 to 40 ?


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is  " + self.name)

p1 = Person("rashi" , 24)

p1.age = 23
print(p1.age)