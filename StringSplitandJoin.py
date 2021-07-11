"""

In Python, a string can be split on a delimiter.

Example:

# >>> a = "this is a string"
# >>> a = a.split(" ") # a is converted to a list of strings.
# >>> print a
['this', 'is', 'a', 'string']
Joining a string is simple:

# >>> a = "-".join(a)
# >>> print a
this-is-a-string

"""


def split_and_join(line):
    # write your code here

    return '-'.join(line.strip().split(' '))


def reverse_words_order_and_swap_cases(sentence):
    return ' '.join(reversed(sentence.split())).strip().swapcase()


print(split_and_join("this is a string "))
print(reverse_words_order_and_swap_cases("aWESOME is cODING"))
