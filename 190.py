# Nested If

# if Statements inside if statements
#this is called nested if statements

x = 41

if x > 10:
    print("10")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20")
else:
    print("less than ten")