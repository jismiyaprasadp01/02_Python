"""
Set the nth Bit of a Number
Write an expression that sets the nth bit of a given integer to 1 (leave other bits unchanged).
Sample Input: n = 9, bit_position = 3
"""
n = 9
bit_position = 3

result = n | (1 << bit_position)

print("Result:", result)
