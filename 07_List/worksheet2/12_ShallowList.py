"""
Task: Write a Python program to flatten a shallow list.
Sample input: [[1, 2], [3, 4], [5, 6]]
Output: [1, 2, 3, 4, 5, 6]
"""
a = [[1, 2], [3, 4], [5, 6]]

result = []

for sub in a:
    result += sub

print(result)
