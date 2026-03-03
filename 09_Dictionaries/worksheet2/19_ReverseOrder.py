'''Reverse the Order
Reverse the order of keys in a dictionary, so the last becomes first and vice versa.
Input: d = {'first': 1, 'second': 2, 'third': 3}
Expected Output: {'third': 3, 'second': 2, 'first': 1}'''
import ast
d=input("Enter the dictionary:")
d=ast.literal_eval(d)
print(dict(reversed(d.items())))
