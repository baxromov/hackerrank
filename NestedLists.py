"""

Given the names and grades for each student in a class of N  students,
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

"""
students = []
for _ in range(int(input("Enter number of students:"))):
    try:
        name = input("Enter Name:")
        score = float(input("Enter student's score:"))
        students.append([name, score])
    except ValueError as e:
        print("Value error:", e)

a = dict(students)

t = {}

for i, j in a.items():
    if j not in t:
        t[j] = [i]
    else:
        t[j].append(i)

new_list = []
for key in sorted(t.keys()):
    new_list.append(t[key])

temp = sorted(new_list[1])
for i in temp:
    print(i)
print("Answer: ", new_list[1])
