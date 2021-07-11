"""

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

"""
open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]
"""
def isValid(s):
    stack = []
    for i in s:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False

"""


def isValid(s):
    stack = []
    for i in s:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if open_list[pos] == stack[len(stack)-1]:
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False

print(isValid("{[(){}]}"))
