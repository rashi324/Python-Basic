#Upadate Dictionary
#The update() method will update the dictionary
# with the items from the given arguments.

#The arguments must be a dictionary,
# or an iterable object with key:value pairs.
#Update the "year" of the car by using the update() method:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)