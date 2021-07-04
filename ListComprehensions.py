"""

Let's learn about list comprehensions! You are given three integers x,y  and
representing the dimensions of a cuboid along with an integer n.
Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the
sum of i+j+k  is not equal to . Here, 0 <= i <= x; 0 <= j <= y; 0 <= k <= z.
Please use list comprehensions rather than multiple loops, as a learning

"""
x = 1
y = 1
z = 2
n = 3

arr_3_D = []

for i in range(x+1):
	for j in range(y+1):
		for k in range(z+1):
			if i+j+k != n:
				arr = [i,j,k]
				arr_3_D.append(arr)


print(arr_3_D)
# [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2]]
