"""
Task: Write a Python program to insert an element at a specified position in a list.
Sample input: [1, 2, 3, 4], element: 5, position: 2
Output: [1, 2, 5, 3, 4]
"""
a = [1, 2, 3, 4]
ele = 5
pos = 2

a.insert(pos, ele)

print(a)
