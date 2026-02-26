"""
Task: Write a Python program to create a list of even numbers from a given list using list comprehension.
Sample input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Output: [2, 4, 6, 8, 10]
"""
a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res=[]
for i in a:
	if i%2==0:
		res=i
		print(res)
