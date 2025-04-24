#Parse JSON - Convert from JSON to Python

#If you have a JSON string,
# you can parse it by using the json.loads() method.

#The result will be a Python dictionary.

# Convert from JSON to python ?

import json

# some JSON:
x = '{"name":"john", "age":30, "city":"New York"}'

# Parse x :
y = json.loads(x)

# the results is a python dictionary:
print(y)
