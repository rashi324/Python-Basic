#Lambda Functions

# function definition to make a function
# that always doubles the number you send in ?


#Function Definition:
def myfunc(n):
  return lambda a : a * n

#myfunc takes one argument n.
# It returns a lambda function, lambda a: a * n,
# which is an anonymous (unnamed) function.
# This lambda takes one argument a and returns the result of a * n.


#Creating a Multiplier:
mydoubler = myfunc(2)


# Here, myfunc(2) is called with n = 2.
# This returns a lambda function equivalent to
# lambda a: a * 2 (because n is 2).
# mydoubler now holds a reference to this lambda function,
# so mydoubler(a) will double any input a.

print(mydoubler(11))



# Calling mydoubler(11) invokes the lambda function with a = 11.
# This calculates 11 * 2, which is 22.
# print outputs 22.