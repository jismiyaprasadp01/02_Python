'''Filter Dictionary Values in Heterogeneous Dictionary
Your dictionary has mixed value types. Filter only the integer values into a new dictionary.
Input: d = {'x': 100, 'y': 'hello', 'z': 200}
Expected Output: {'x': 100, 'z': 200}'''

import ast
d=input("Enter the dictionary 1:")
d=ast.literal_eval(d)

d1 = dict(filter(lambda item: isinstance(item[1], int), d.items()))
print(d1)
