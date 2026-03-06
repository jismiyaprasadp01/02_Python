"""
Task: Write a Python function to check if a given list is a palindrome (reads the same forwards and backwards).
Sample input: [1, 2, 3, 2, 1]
Output: True
"""
a=[1,2,3,2,1]
if a==a[::-1]:
	print("palindrome")
else:
	print("not palindrome")
