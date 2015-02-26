#!/usr/bin/python

i = input("Enter an int: ")
# is i actually an integer?
if(not isinstance(i, (int, long))):
    print("'" + i + "' is not an int")
elif(i == 0):
    print("Attempt to divide by zero")
else:
    result = 100/i  # we know i is an int != 0
    print(result)



