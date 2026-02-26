"""
For n rows, print a right-aligned triangle pattern
    *
   **
  ***
 ****
*****
"""
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)
