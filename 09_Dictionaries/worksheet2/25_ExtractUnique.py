'''Extract Unique Dictionary Values
Extract all unique values from the dictionary. How many distinct items are there?
Input: d = {'a': 1, 'b': 2, 'c': 2, 'd': 3}
Expected Output: [1, 2, 3]'''

import ast
d=input("Enter the dictionary 1:")
d=ast.literal_eval(d)

print(list(set(d.values())))
