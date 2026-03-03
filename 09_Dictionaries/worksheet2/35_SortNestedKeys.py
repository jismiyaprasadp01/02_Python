''' Sort Nested Keys by Value
Sort the keys inside each nested dictionary by their value.
Input: d = {'group1': {'b': 2, 'a': 1}, 'group2': {'c': 3, 'd': 0}}
Expected Output: {'group1': [('a', 1), ('b', 2)], 'group2': [('d', 0), ('c', 3)]}'''

import ast
d=input("Enter the list of dictionary:")
d=ast.literal_eval(d)
d1={}
for i,k in d.items():
    d1[i]=sorted(k.items(),key=lambda x:x[1])
print(d1)

