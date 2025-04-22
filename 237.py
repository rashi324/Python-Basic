#The self Parameter!
#The self parameter is a reference to the current instance of the class,
# and is used to access variables that belongs to the class.
#It does not have to be named self ,
# you can call it whatever you like,
# but it has to be the first parameter of any function in the class:
# Use the words mysillyobject and abc instead of self ?


class Person:
    def __init__(sillyobject, name, age):
        sillyobject.name = name
        sillyobject.age = age

    def myfunc(abc):
        print("Hello my name is  " + abc.name)

p1 = Person("rashi" , 24)
p1.myfunc()