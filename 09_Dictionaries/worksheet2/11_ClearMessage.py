'''Empty Desk Detective
You check a colleague's desk (dictionary) for items. If it's empty, print a clear message so you don't miss anything!
Input: desk = {}
Expected Output: Dictionary is empty!'''

import ast
desk=input("Enter the desk details:")
desk=ast.literal_eval(desk)

if not len(desk):
    print("Dictionary is empty")
else:
    print("Dictionary is Not empty,values are:",desk)
