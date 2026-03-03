"""
Description: Check whether all elements in a tuple are unique using set comparison.
Ensures data integrity in scenarios where duplicate values are not allowed.
Input: t = (1, 2, 3, 4, 5)
Output: True
"""
t = (1, 2, 3, 4, 5)
result = len(t) == len(set(t))
print(result)
