"""
Description: Change the last value in every tuple in a list to a given value.
This shows how to modify immutable data structures by reconstructing them.
Input: lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)], New value: 100
Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
"""
lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
new_value = 100
updated_list = [t[:-1] + (new_value,) for t in lst]
print(updated_list)
