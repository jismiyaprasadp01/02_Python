"""
Task: Write a Python function to reverse a list at a specific location.
Sample input: [1, 2, 3, 4, 5, 6], position: 3
Output: [1, 2, 3, 6, 5, 4]
"""
a = [1, 2, 3, 4, 5, 6]
pos = 3

first_part = a[:pos]
second_part = a[pos:]

second_part.reverse()

result = first_part + second_part

print(result)
