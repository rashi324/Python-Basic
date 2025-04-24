#The search() Function

#The search() function searches the string for a match,
# and returns a Match object if there is a match.

#If there is more than one match,
# only the first occurrence of the match will be returned:

#Search for the first white-space character in the string ?


import re

txt = "The rain in Spain"
x = re.search("\s", txt)

# \s ---Returns a match where the string contains a white space character

print("The first white-space character is located in position:",
      x.start())