"""
Task: Write a Python program to combine two lists into a dictionary.
Sample input: ['a', 'b', 'c'], [1, 2, 3]
Output: {'a': 1, 'b': 2, 'c': 3}
"""
keys = ['a', 'b', 'c']
values = [1, 2, 3]

result = dict(zip(keys, values))

print(result)
