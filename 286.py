#The sub() Function

#The sub() function replaces the matches with the text of your choice:

#Replace every white-space character with the number 9 ?

import re

txt = "The rain in spian"
x = re.sub("\s", "9", txt)
print(x)