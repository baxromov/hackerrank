"""

The provided code stub will read in a dictionary containing key/value
pairs of name:[marks] for a list of students. Print the average of the
marks array for the student name provided, showing 2 places after the decimal.

"""
from decimal import Decimal

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores


query_name = input()
new_dict = []
for key, val in student_marks.items():
    if query_name in key:
        new_dict.append([key, val])

temp = []
a = 0
for i in new_dict:
    x, y = i
    a = round((Decimal(sum(y)))/3, 2)


print(a)
