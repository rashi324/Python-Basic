# The __str__() Function

# The __str__() function controls what should be returned
# when the class object is represented as a string.

# If the __str__() function is not set,
# the default string representation of the object is returned:

# The string representation of an object WITHOUT the __str__() function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("john", 36)
print(p1)  # This will print something like: <__main__.Person object at 0x...>

# The string representation of an object WITH the __str__() function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

p1 = Person("john", 36)
print(p1)  # This will print: john (36)

