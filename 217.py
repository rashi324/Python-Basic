#Recursion
#Python also accepts function recursion,
# which means a defined function can call itself.

# Example of a recursive function-

def factorial(x):

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

num = 5
print("the factorial of" , num, "is", factorial(num))



#Putting it all together:5*4*3*2*1
# factorial of 5 = 1*2*3*4*5 =6





# factorial of 5

#Step-by-Step Execution


# factorial(5) calls factorial(4),
# so it waits for factorial(4) to complete.

# factorial(4) calls factorial(3).

# factorial(3) calls factorial(2).

# factorial(2) calls factorial(1).

# factorial(1) reaches the base case, so it returns 1.




# Now, the recursive calls start returning back up:

# factorial(2) gets 1 from factorial(1), so it returns 2 * 1 = 2.
# factorial(3) gets 2 from factorial(2), so it returns 3 * 2 = 6.
# factorial(4) gets 6 from factorial(3), so it returns 4 * 6 = 24.
# factorial(5) gets 24 from factorial(4), so it returns 5 * 24 = 120.
# So, factorial(5) returns 120, which is printed as the result.