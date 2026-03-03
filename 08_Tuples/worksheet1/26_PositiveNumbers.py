"""
Description: From a list of tuples, keep only those where all numbers are positive.
Filtering based on condition is commonly used for cleaning or selecting data.
Input: lst = [(1, 2), (-3, 4), (5, 6)]
Output: [(1, 2), (5, 6)]
"""
lst = [(1, 2), (-3, 4), (5, 6)]
result = [t for t in lst if all(num > 0 for num in t)]
print(result)
