#Update Tuples

#Change Tuple Values
#Once a tuple is created, you cannot change its values.
#Tuples are unchangeable, or immutable as it also is called.

# You can convert the tuple into a list,
# change the list, and convert the list back into a tuple.

#Convert the tuple into a list to be able to change it?


x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)