"""
Rotate Bits Left by k Positions
Given a number (assume 8 bits) and a value k, write an expression to rotate its bits to the left by k positions.
Sample Input: n = 150, k = 2
"""
n=150
k=2
result=((n<<k)|(n>>(8-k)))&0xFF
print("Result is ",result)
