''' Log Session Nested Dictionary from List
Given a list, build a nested dictionary where each item is a deeper level (like a Russian doll).
Input: list = ['a', 'b', 'c', 'd']
Expected Output: {'a': {'b': {'c': {'d': {}}}}}'''
import ast
list =input("Enter the list:")
list=ast.literal_eval(list)

nested = {}
for item in reversed(list):
    nested = {item: nested}

print(nested)
