"""

Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
You are given  scores. Store them in a list and find the score of the runner-up.

"""


n = int(input("Enter: "))
arr = map(int, input("Enter arr: ").split())

arr_list = sorted(list(arr))
one_to_ten = sorted(list(set(arr_list[-n:])))
runner_up = one_to_ten[-2]
print(arr_list)
print(one_to_ten)
print("The second place", runner_up)

