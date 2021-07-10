"""

Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of
commands where each command will be of the 7 types listed above. Iterate
through each command in order and perform the corresponding operation on your list.

"""

arr = []
cmd = ['insert', 'print', 'remove', 'append', 'sort', 'pop', 'reverse']

n = range(int(input("N:")))
new_list = []
for i in n:
    arr.append(input().split())

for k in range(len(arr)):
    if arr[k][0] == 'insert':
        new_list.insert(int(arr[k][1]), int(arr[k][2]))
    elif arr[k][0] == 'print':
        print(new_list)
    elif arr[k][0] == 'remove':
        new_list.remove(int(arr[k][1]))
    elif arr[k][0] == 'append':
        new_list.append(int(arr[k][1]))
    elif arr[k][0] == 'sort':
        new_list.sort()
    elif arr[k][0] == 'pop':
        new_list.pop()
    elif arr[k][0] == 'reverse':
        new_list.reverse()


print(new_list)
