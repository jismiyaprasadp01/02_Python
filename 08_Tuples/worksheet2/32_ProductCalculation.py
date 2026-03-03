"""
Description: Calculate the product by multiplying all the numbers in a tuple.
This is useful for aggregate calculations and is commonly found in mathematical programming and statistics.
Input: t = (4, 3, 2, 2, -1, 18)
Output: -864
"""
t = (4, 3, 2, 2, -1, 18)
product = 1
for num in t:
    product *= num
print(product)
