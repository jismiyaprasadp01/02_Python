"""
Print the sum of all odd numbers from 1 up to n (inclusive), using loops only.
"""
n = int(input())
total = 0

for i in range(1, n + 1):
    if i % 2 != 0:
        total += i

print(total)
