"""


Mr. Vincent works in a door mat manufacturing company.
One day, he designed a new door mat with the following specifications:

- Mat size must be MxN. (N is an odd natural number, and M is 3 times .)
- The design should have 'WELCOME' written in the center.
- The design pattern should only use |, . and - characters.

- 5 < N < 101
- 15 < M < 303

Sample Input:
9 27

Sample Output:

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------


"""
import math

N, M = map(int, input().split())
c, dash, welcome = '.|.', '-', 'welcome'.upper()

if (N < 5 or N > 101) and (M < 15 or M > 303):
    print("Error! \n5 < N < 101 , 15 < M < 303")
else:
    for i in range(0, math.floor(int(N) / 2)):
        s = c * i
        print(s.rjust(math.floor((M - 2) / 2), dash) + c + (c * i).ljust(math.floor((M - 2) / 2), dash))
    print(welcome.center(M, dash))

    for i in reversed(range(0, math.floor(int(N) / 2))):
        s = c * i
        print(s.rjust(math.floor((M - 2) / 2), dash) + c + (c * i).ljust(math.floor((M - 2) / 2), dash))
