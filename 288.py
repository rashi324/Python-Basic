#Match Object

#A Match Object is an object containing
# information about the search and the result.
# If there is no match,
# the value None will be returned, instead of the Match Object.

#Do a search that will return a Match Object ?

import re

txt = "The rain in Spian"
x = re.search("ai", txt)
print(x)