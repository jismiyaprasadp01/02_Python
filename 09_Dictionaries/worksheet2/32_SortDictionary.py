'''Sort Dictionary Keys and Values List
Sort a dictionary by keys, and also sort the values list of each key.
Input: d = {'c': [3,1], 'a': [2,4], 'b': [5,1]}
Expected Output: [('a', [2,4]), ('b', [1,5]), ('c', [1,3])]'''

from collections import defaultdict
import ast
d=input("Enter the dictionary:")
d=ast.literal_eval(d)
d1=defaultdict(list)

d=dict(sorted(d.items()))

for i,j in d.items():
    d1[i]=sorted(j)

print(list(d1.items()))

