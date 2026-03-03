'''Remove Keys with Substring
Remove all keys from the dictionary that contain a certain substring (like a keyword filter).
Input: d = {'sun': 1, 'sunny': 2, 'rain': 3}, substring = 'sun'
Expected Output: {'rain': 3}'''

import ast
d=input("Enter the dictionary:")
d=ast.literal_eval(d)
n=input("Enter the keyword filter:")
d1={}
for i,j in d.items():
    if n not in i:
        d1[i]=j

print(d1)
