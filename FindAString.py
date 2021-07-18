"""

In this challenge, the user enters a string and a substring.
You have to print the number of times that the substring occurs in the given string.
String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

"""


def count_substring(string, sub_string):
    c = 0
    # string, sub_string = string.upper(), sub_string.upper()
    for i in range(0, len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            c += 1
    return c


print(count_substring("In the convential world, it won't ever happen", 'lD,'))
