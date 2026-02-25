"""
Use the Ternary Operator to Find the Minimum of Two Numbers
Use a single expression to find the smaller of two numbers.
Sample Input: a = 20, b = 13
"""
a,b=map(int,input("Enter a b").split())
#min=b if a>b else a
min=min(a,b)
print(min)
