#check if key Exists

#To determine if a specified key is present in
# a dictionary use the in keyword:

#Check if "model" is present in dictionary ?

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("yes, 'model' is one of the keys in the thisdict dictionary")
else:
    print("not in thisdict")