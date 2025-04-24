#You can also define the separators,

# default value is (", "     ": "),

# which means using a comma and a space to separate each object,
# and a colon and a space to separate keys from values:

# Use the separators parameter to change the default separator ?


import json

x = {
    "name": "rashi",
    "age": 24,
    "married": True,
    "divorced": False,
    "children" : ("Ann", "Billy"),
    "pets":None ,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]

}

# use . and a space to separate objects,
# and a space, a = and a space to separate keys from their values:


print(json.dumps(x, indent=4, separators=(". ", " = ")))