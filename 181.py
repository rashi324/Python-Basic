#Elif
#The elif keyword is python's way of saying
# "if the previous conditions were not true,
# then try this condition".

a = 33
b = 33
if b > a:
    print("b is grater than a")
elif a == b:
    print("a and b are equal")
else: #elif a > b:
    print("nothing ok")