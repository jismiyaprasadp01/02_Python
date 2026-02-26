"""
Check if a given number is a perfect number (sum of divisors excluding itself), using only loops.
"""
n = int(input())
total = 0

for i in range(1, n):
    if n % i == 0:
        total += i

if total == n:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
