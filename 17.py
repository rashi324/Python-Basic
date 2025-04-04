#local variables

def myfunc1():
    z = "fantastic"
    #z is an local variables, can be accesed only inside function.
    print(z)

myfunc1()

#global keyword
def myfunc():
    global  x
    x = "fantastic"
myfunc()
print("python is " +  x)