'''Substring Key Find
Given a search term, find out which keys in your dictionary contain it. Useful for partial name search!
Input: d = {'hello': 1, 'world': 2, 'hell': 3}, s = 'hell'
Expected Output: Keys containing 'hell': ['hello', 'hell']'''
import ast
d=input("Enter the dictionary details:")
d=ast.literal_eval(d)
s = input("Enter the substring for partial name search:")

matching_keys = [key for key in d if s in key]

print(f"Keys containing '{s}': {matching_keys}")
