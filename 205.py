#Else in For Loop

#The else keyword in a for loop specifies
# a block of code to be executed when the loop is finished:
#Print all numbers from 0 to 5,
# and print a message when the loop has ended ?

for x in range(6):
    print(x)
else:
    print("finally finished")

    # the else block will Not be executed if the loop
    # is stopped by a break statement