'''Sort Dictionaries List by Key’s Value List Index
Given a list of dictionaries, sort them by the value at a specific index in each key’s value list.
Input: dicts = [{'a': [5,1]}, {'a': [3,4]}, {'a': [7,0]}], index = 1
Expected Output: [{'a': [7,0]}, {'a': [5,1]}, {'a': [3,4]}]'''

import ast
d=input("Enter the list of dictionary:")
d=ast.literal_eval(d)

d.sort(key=lambda x: x['a'][1])

print(d)
