#You can use the ^ operator
# instead of the symmetric_difference() method,
# and you will get the same result.


#Use ^ to join two sets ?

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2

print(set3)

# The ^ operator only allows you to join sets with sets,
# and not with other data types
# like you can with the symmetric_difference() method.

