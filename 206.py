#Nested Loops
#A nested loop is a loop inside a loop.

#The "inner loop" will be executed
# one time for each iteration of the "outer loop":


#Print each adjective for every fruit ?


adj = ["red","big","testy"]
fruits = ["apple","banana","cherry"]

for x in adj:
    for y in fruits:
        print(x,y)