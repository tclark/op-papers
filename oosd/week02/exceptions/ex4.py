#!/usr/bin/python

i = input("Enter an int: ")
while(i == 0):
    print("You can't divide by zero.")
    i = input("Enter an int (not zero): ")

try:
    result = 100/i  # we know i is != 0, but it might not be an int
    print(result)
except TypeError:
    print("'" + i + "' is not an int.")



