#perform a case-insensitive sort of the list:

thislist = ["banana", "Orange", "kiwi", "cherry"]

thislist.sort(key = str.lower)

print(thislist)

#The key parameter is set to str.lower,
# which means that the list will be sorted based
# on the lowercase version of each string element.

#"banana".lower() returns "banana"
#"Orange".lower() returns "orange"
#"Kiwi".lower() returns "kiwi"
#"cherry".lower() returns "cherry"