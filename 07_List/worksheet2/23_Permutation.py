"""
Task: Write a Python function that generates all the permutations of the elements in a given list.
Sample input: [1, 2, 3]
Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
"""
from itertools import permutations

def generate_permutations(lst):
    return [list(p) for p in permutations(lst)]

nums = [1, 2, 3]
print(generate_permutations(nums))
