#Print the string passed into the function ?

import re

txt = "The rain in Spian"
x = re.search(r"\bS\w+", txt)
print(x.string)