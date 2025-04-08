#Remove List Items
#This remove() method removes the specified item.

#Remove "banana"?

thislist = ["apple","banana", "cherry"]
thislist.remove("banana")
print(thislist)

#If there are more than one item with the specified value,
# the remove() method removes the first occurance:

#Remove the first occurance of "banana"?
thislist1 =  ["apple","banana", "cherry", "banana", "kiwi"]
thislist1.remove("banana")
print(thislist1)