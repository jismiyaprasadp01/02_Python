"""
Task: Write a Python program to remove all occurrences of a specific element from a list.
Sample input: [1, 2, 3, 2, 4, 2, 5], element to remove: 2
Output: [1, 3, 4, 5]
"""
a=[1, 2, 3, 2, 4, 2, 5]
n=2
res=[]
for i in a:
	if i!=n:
		res=i
		print(res)
