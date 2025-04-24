#The findall() Function

#The findall() function returns a list containing all matches.

#Print a list of all matches ?

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)

print(x)