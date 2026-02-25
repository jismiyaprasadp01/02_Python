"""
Evaluate a Quadratic Expression
Given values for x, a, b, and c, write an expression to compute ax² + bx + c.
Sample Input: a = 2, b = 3, c = 4, x = 5
"""
#a, b, c, x = map(int,['2','3','4','5'])
a,b,c,x=map(int,(input("Enter a b c x")).split())
u = a * (pow(x, 2)) + b * x + c
print("Result:", u)
