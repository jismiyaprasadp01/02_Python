'''Dictionary with Most Pairs
Given multiple dictionaries, find the one with the most key-value pairs (the biggest dictionary wins).
Input: dicts = [{'a': 1, 'b': 2}, {'x': 1, 'y': 2, 'z': 3}, {'k': 9}]
Expected Output: {'x': 1, 'y': 2, 'z': 3}'''
import ast
d=input("Enter the dictionary:")
d=ast.literal_eval(d)
d1={}
max=0
for i in d:
    if len(i)>max:
        max=len(i)
        d1=i

print(d1)
