#!/usr/bin/python

i = input("Enter an int: ")
# is i actually an integer?

try:
    result = 100/i  # what if i is 0?
    print(result)
except TypeError:
    print("'" + i + "' is not an int.")
except ZeroDivisionError as e:
    print(e)
finally:
    print("We're done.")




