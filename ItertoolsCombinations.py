"""


itertools.combinations(iterable, r)
This tool returns the r length subsequences of elements from the input iterable.

Combinations are emitted in lexicographic sorted order.
So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

Task

You are given a string S.
Your task is to print all possible combinations, up to size , of the string in lexicographic sorted order.

Input Format

A single line containing the string S and integer value k separated by a space.

Constraints


The string contains only UPPERCASE characters.

Output Format

Print the different combinations of string S on separate lines.


"""
from itertools import combinations

s, k = input().split()

for j in range(1, int(k)+1):
    for i in list(combinations(sorted(s.upper()), j)):
        print("".join(i))
