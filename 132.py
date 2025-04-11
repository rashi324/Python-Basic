#Join a set and a Tuple

#The union() method allows you to join a set with other data types,
#like lists or Tuples.

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)