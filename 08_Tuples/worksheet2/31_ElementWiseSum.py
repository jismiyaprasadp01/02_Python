"""
Description: Compute the element-wise sum of multiple tuples of equal length.
This exercise teaches how to combine tuples by adding corresponding elements, often used in mathematical and data processing tasks.
Input: t1 = (1, 2, 3, 4), t2 = (3, 5, 2, 1), t3 = (2, 2, 3, 1)
Output: (6, 9, 8, 6)
"""
t1 = (1, 2, 3, 4)
t2 = (3, 5, 2, 1)
t3 = (2, 2, 3, 1)
result=tuple(a+b+c for a,b,c in zip(t1,t2,t3))
print(result)
