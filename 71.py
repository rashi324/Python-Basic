#List Comprehension

#List comprehension offers a shorter syntax
# when you want to create a new list based on the
# values of an existing list.


#  The Syntax
#     newlist = [expression for item in iterable if condition == True]


# you want a new list,
# containing only the fruits with the letter "a" in the name.

#Without list comprehension
#You will have to write a for statement with a conditional test inside:

fruits = [ "apple", "banana", "cherry", "kiwi","mango"]
newlist = []

for x in fruits:
    if "a" in x :
        newlist.append(x)
print(newlist)

#using list comprehension

fruits1 = [ "apple", "banana", "cherry", "kiwi","mango"]

newlist1 = [x for x in fruits1 if "a" in x]

print(newlist1)