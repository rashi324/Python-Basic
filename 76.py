#Return "orange" instead of "apple" ?

fruits = ["apple", "banana", "cherry","kiwi","mango","banana"]

newlist = [x if x != "apple" else "orange" for x in fruits]

print(newlist)