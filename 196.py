# The continue Statement

# with The continue statement we can stop current iteration

# and continue with the next

#continue to the next iteration if i is 3

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)