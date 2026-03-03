'''Robot Warehouse – Fast Inventory Sum
A robot does inventory at the end of the day and must tell the boss the total number of items, 
not just per item. What’s the fastest way for the robot to add up all item counts in the warehouse?
Input: inventory = {'box': 30, 'crate': 22, 'pallet': 8}
Expected Output: Total items in warehouse: 60'''

import ast
inventory=input("Enter the inventory details:")
inventory=ast.literal_eval(inventory)

print("the total items in warehouse:",sum( inventory.values()))
