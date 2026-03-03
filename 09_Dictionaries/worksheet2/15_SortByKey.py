'''Sort by Key
Organize a scrambled dictionary by key order so that the output is sorted by key.
Input: d = {'b': 2, 'a': 1, 'c': 3}
Expected Output: [('a', 1), ('b', 2), ('c', 3)]'''

import ast
d=input("Enter the dictionary details:")
d=ast.literal_eval(d)
print(sorted(d.items()))
