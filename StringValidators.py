"""

Python has built-in string validation methods for basic data.
It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.

str.isalnum()
This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).

str.isalpha()
This method checks if all the characters of a string are alphabetical (a-z and A-Z).

str.isdigit()
This method checks if all the characters of a string are digits (0-9).

str.islower()
This method checks if all the characters of a string are lowercase characters (a-z).

str.isupper()
This method checks if all the characters of a string are uppercase characters (A-Z).

0 < len(s) < 1000


The any() function is an inbuilt function in Python which returns true
if any of the elements of a given iterable
( List, Dictionary, Tuple, set, etc) are True else it returns False.


"""


s = 'qA2'

if len(s) > 0 and len(s) < 1000:
    print(any([i.isalnum() for i in s]))
    print(any([i.isalpha() for i in s]))
    print(any([i.isdigit() for i in s]))
    print(any([i.islower() for i in s]))
    print(any([i.isupper() for i in s]))
























