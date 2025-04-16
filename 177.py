#Create three dictionaries ?
#then create one dictionary that will contain
#the other three dictionaries?
child1 = {
    "name" : "ayana",
    "year" : 2003
}
child2 = {
    "name" : "rashi",
    "year" : 2001
}
child3 = {
    "name" : "ayra",
    "year" : 2028
}
mychild = {
    "child1" : child1,
    "child2": child2,
    "child3": child3
}
print(mychild)