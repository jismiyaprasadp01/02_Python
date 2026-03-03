'''Append Dictionary Keys and Values
Append the keys and values of one dictionary to another, keeping the order. Build a bigger dictionary!
Input: d1 = {'one': 1, 'two': 2}, d2 = {'three': 3, 'four': 4}
Expected Output: {'one': 1, 'two': 2, 'three': 3, 'four': 4}'''
import ast
d=input("Enter the dictionary 1:")
d=ast.literal_eval(d)
d1=input("Enter the dictionary 2:")
d1=ast.literal_eval(d1)
d.update(d1)
print(d)
