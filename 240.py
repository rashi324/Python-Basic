#Delete Objects
#You can delete objects by using the del keyword:

#Delete the p1 object ?

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is  " + self.name)

p1 = Person("rashi" , 24)

del p1
print(p1)