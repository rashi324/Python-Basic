# the continue statement

# with the continue statement we can stop
# the current iteration of the loop
# and continue with the next

# do not print banana

fruits = ["apple","banana","cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)