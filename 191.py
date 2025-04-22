# 3 if condition

x = 41
if x > 10:
    print("10")
    if x > 20:
        print("and also above 20!")
        if x > 30:
            print("and also above 30")
        else:
            print("not above 30")
    else:
        print("but not above 20.")
else:
    print("less than ten")