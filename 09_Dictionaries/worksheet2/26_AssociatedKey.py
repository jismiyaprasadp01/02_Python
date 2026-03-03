'''Keys Associated with Values
Find all keys that share the same value. Group keys by their values.
Input: d = {'m': 1, 'n': 2, 'o': 1}
Expected Output: {1: ['m', 'o'], 2: ['n']}'''
from collections import defaultdict

import ast
d=input("Enter the dictionary 1:")
d=ast.literal_eval(d)

grouped = defaultdict(list)

for key, value in d.items():
    grouped[value].append(key)
    
print(dict(grouped))
