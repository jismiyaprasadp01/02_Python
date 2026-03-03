"""
Description: Perform elementwise AND and XOR operations between two tuples of integers of equal length.
Elementwise bitwise operations are crucial in low-level data processing and algorithm optimization.
Input: t1 = (1, 2, 3), t2 = (2, 2, 2)
Output: AND: (0, 2, 2), XOR: (3, 0, 1)
"""
t1 = (1, 2, 3)
t2 = (2, 2, 2)
and_result = tuple(a & b for a, b in zip(t1, t2))
xor_result = tuple(a ^ b for a, b in zip(t1, t2))
print("AND:", and_result)
print("XOR:", xor_result)
