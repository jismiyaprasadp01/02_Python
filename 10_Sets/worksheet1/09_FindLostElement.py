"""
Python Set difference to find lost element from a duplicated array
Story: You had four marbles yesterday, now one is missing. Which one?
Sample Input
yesterday = [1, 2, 3, 4]
today = [1, 4, 2]
Sample Output
3
"""

a= [1, 2, 3, 4]
b= [1, 4, 2]
lis=set(a)-set(b)
print(lis)
