#Convert a Python object containing all the legal data types ?

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
print(json.dumps(x))