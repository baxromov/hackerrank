"""

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

"""


def isValid(s):
    new_list = []
    signs = ['(', ')', '[', ']', '{', '}']
    ascii_code = []
    for i in signs:
        ascii_code.append(ord(i))
    print(ascii_code)

    for i in s:
        new_list.append(i)

    new_list_ascii = []
    for i in new_list:
        new_list_ascii.append(ord(i))

    print(new_list_ascii)

    if (new_list.count(signs[0]) == new_list.count(signs[1]) and new_list.count(signs[2]) == new_list.count(signs[3]) and new_list.count(signs[4]) == new_list.count(signs[5])) and new_list_ascii == sorted(new_list_ascii):
        return True



    return False


print(isValid("()[]"))
print(ord('('), '-', ord(')'))
print(ord('['), '-', ord(']'))
print(ord('{'), '-', ord('}'))
