#Access Items in Nested Dictionaries
#Print the name of child 2 ?

myfamily = {
    "child1" : {
        "name" : "email",
        "year" : 2004
    },
    "child2": {
        "name": "Tobins",
        "year": 2008
    },
    "child3": {
        "name": "annu",
        "year": 2005
    }
}
print(myfamily["child1"]["name"])