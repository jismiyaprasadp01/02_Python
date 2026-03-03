'''The Cafe’s Popular Menu
Every order is tracked in a list. Can you build a menu board that shows how many times each item was ordered today?
Input: orders = ['latte', 'espresso', 'latte', 'tea', 'espresso', 'latte']
Expected Output: {'latte': 3, 'espresso': 2, 'tea': 1}'''
import ast
orders=input("Enter the orders details:")
orders=ast.literal_eval(orders)
d={}
for i in orders:
    d[i]=d.get(i,0)+1
print("Output:",d)
