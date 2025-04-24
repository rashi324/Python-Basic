#Convert from Python to JSON
#If you have a Python object,

# you can convert it into a JSON string by
# using the json.dumps() method.

#Convert from Python to JSON?
import json
# a python object (dict):
x = {
    "name": "jhon",
    "age": 30,
    "city": "New York"
}

# convert into JSON :
y = json.dumps(x)

# the result is a JSON string:
print(y)