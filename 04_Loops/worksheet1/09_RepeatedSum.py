"""
Take an integer and, using only loops, sum its digits repeatedly until only a single digit remains.
Example: 9875 → 9+8+7+5=29 → 2+9=11 → 1+1=2
"""
n = int(input("Enter an integer: "))

n = abs(n)

while n >= 10:
    digit_sum = 0
    while n > 0:
        digit_sum += n % 10
        n //= 10
    n = digit_sum

print("Single digit result:", n)
