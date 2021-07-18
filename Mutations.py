"""

We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).

Let's try to understand this with an example.

You are given an immutable string, and you want to make changes to it.

Example

string = "abracadabra"
You can access an index by:

print string[5]
a

"""


def mutate_string(string, position, character):
    new_list = list(string)
    new_list[position] = character

    return ''.join(new_list).strip()


print(mutate_string("Saom", 2, 'l'))
