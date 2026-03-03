'''Flip Nested Dictionary
Given a nested dictionary, swap the outer and inner keys. Who becomes the new outer boss?
Input: d = {'x': {'p': 1}, 'y': {'q': 2}}
Expected Output: {'p': {'x': 1}, 'q': {'y': 2}}'''

import ast
d=input("Enter the nested dictionary:")
d=ast.literal_eval(d)

flipped={}

for i,j in d.items():
    for n,k in j.items():
        if n not in flipped:
            flipped[n]={}
        flipped[n][i]=k
print(flipped)
