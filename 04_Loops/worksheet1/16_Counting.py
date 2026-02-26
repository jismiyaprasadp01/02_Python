"""
nput an integer and count how many times 0 appears in it (no strings or lists).
"""
n = int(input())
count = 0

while n > 0:
    digit = n % 10
    if digit == 0:
        count += 1
    n //= 10

print(count)
