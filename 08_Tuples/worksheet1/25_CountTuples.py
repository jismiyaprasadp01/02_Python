"""
Description: Count the number of tuples where every element is divisible by a given integer K.
This builds filtering skills and strengthens logic construction for data validation.
Input: lst = [(3, 6), (9, 12, 15), (4, 8)], K = 3
Output: 2
"""
lst = [(3, 6), (9, 12, 15), (4, 8)]
K = 3
count = sum(1 for t in lst if all(num % K == 0 for num in t))
print(count)
