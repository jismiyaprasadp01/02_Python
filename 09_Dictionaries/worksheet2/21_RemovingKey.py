'''Remove High-Value Keys
Remove all keys whose value is greater than a given number. Ignore non-numeric values.
Input: d = {'a': 5, 'b': 10, 'c': 15, 'd': 'big'}, limit = 10
Expected Output: {'a': 5, 'b': 10, 'd': 'big'}'''

import ast
d=input("Enter the dictionary:")
d=ast.literal_eval(d)
n=int(input("Enter the limit:"))
d1={}
for i,j in d.items():
    if  not isinstance(j,(int,float)):
        d1[i]=j
    if (type(j) == int) and j<= n:
        d1[i]=j

    
print(d1)
