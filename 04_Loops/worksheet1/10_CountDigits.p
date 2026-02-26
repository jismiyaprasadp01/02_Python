"""
Input a number and count how many digits it contains, using only arithmetic and loops.
"""
n = int(input("Enter a number: "))

n = abs(n)

if n == 0:
    count = 1
else:
    count = 0
    while n > 0:
        n //= 10
        count += 1

print("Number of digits:", count)
