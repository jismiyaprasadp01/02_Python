"""
Toggle a Specific Bit in an Integer
Given a number and a bit position, write an expression to toggle (flip) that bit.
Sample Input: n = 12, bit_position = 2
"""
n=12
pos=2
res=n^(1<<pos)
print("Result is ",res)
