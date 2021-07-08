"""

A string is a palindrome if it is identical forward and backward. For example “anna”,
“civic”, “level” and “hannah” are all examples of palindromic words. Write a program
that reads a string from the user and uses a loop to determine whether or not it is a
palindrome. Display the result, including a meaningful output message.

"""


def is_String_Polindrome(str):
    return True if str == str[::-1] else False


print(is_String_Polindrome("level"))
