#Print the position(start- and end-position) of
# the first match occurrence!

#The regular expression looks for any words
# that starts with an upper case "S" ?

import re

txt = "The rain in Spian"
x = re.search(r"\bS\w+", txt)
print(x.span())