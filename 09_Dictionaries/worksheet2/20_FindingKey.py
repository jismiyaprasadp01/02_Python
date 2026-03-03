'''Key Present in List and Dictionary
Given a list and a dictionary, extract values for all keys that appear in both.
Input: dict = {'a': 100, 'b': 200, 'c': 300}, lst = ['b', 'c', 'l']
Expected Output: {'b': 200, 'c': 300}'''

import ast
d=input("Enter the dictionary:")
d=ast.literal_eval(d)
l=input("Enter the list:")
l=ast.literal_eval(l)
d1={}
for i in l:
    if i in d.keys():
        d1[i]=d[i]
print(d1)
