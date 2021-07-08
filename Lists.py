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
for i in range(int(input())):
    s = input().split()
    for j in range(1, len(s)):
        if s[0] == 'insert':
            arr.insert(i, s[j])
        elif s[0] == 'print':
            print(arr)
        elif s[0] == 'remove':
            arr.remove(s[j])
        elif s[0] == 'append':
            arr.append(s[j])
        elif s[0] == 'pop':
            arr.pop()
        elif s[0] == 'sort':
            arr.sort()
        elif s[0] == 'reverse':
            arr.reverse()

