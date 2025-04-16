#Loop Through Nested Dictionaries

#You can loop through a dictionary
# by using the items() method like this.

#Loop through the keys and values of all nested dictionaries?

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

for x , z in myfamily.items():
    print(x)

    for y in z :
        print(y+ ':' , z[y])