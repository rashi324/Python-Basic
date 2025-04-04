#The format() method takes unlimited numbers of arguments,
# and are placed into the respective placeholder:

quantity = 3
itemno = 567
price = 49.95

myorder = "I want {} pieces of item {} for {} dollars."

print(myorder.format(quantity, itemno, price))