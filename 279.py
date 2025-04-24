#Search the string to see if it starts with
# "The" and ends with "spain" ?

import re

txt = "The rain in Spain"

x = re.search("The.*Spain$", txt)
if x:
    print("YES! We have a match")
else:
    print("No Match")



#  ^ -----	Starts with
#  .  ------	Any character (except newline character)
#  *  -------	Zero or more occurrences
#  $ ------	Ends with