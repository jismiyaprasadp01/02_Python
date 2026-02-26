"""
Task: Write a Python program to find the common elements between two lists.
Sample input: [1, 2, 3, 4], [3, 4, 5, 6]
Output: [3, 4]

"""
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

result = list(set(a) & set(b))

print(result)
