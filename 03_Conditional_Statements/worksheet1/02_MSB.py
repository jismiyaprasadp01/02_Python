"""
Take an 8-bit register value and print if the **MSB** (most significant bit) is set or not.
Input: 0b10010010
Output: MSB set
"""
n=0b10010010
if n&(1<<7):
	print("MSB is set")
else:
	print("MSB is not set")

