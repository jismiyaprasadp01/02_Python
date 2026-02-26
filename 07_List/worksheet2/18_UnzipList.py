"""
Task: Write a Python program to unzip a list of tuples into individual lists.
Sample input: [(1, 'a'), (2, 'b'), (3, 'c')]
Output: [1, 2, 3], ['a', 'b', 'c']
"""
data = [(1, 'a'), (2, 'b'), (3, 'c')]

list1, list2 = zip(*data)

print(list(list1))
print(list(list2))
