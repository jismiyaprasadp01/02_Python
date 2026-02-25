"""
Find the Second Largest of Three Numbers
Write an expression (no functions, no if) to get the second largest value among three numbers.
Sample Input: a = 20, b = 12, c = 18
"""
a,b,c=20,10,18
max=(a*(a>=b and a>=c))+(b*(b>=a and b>=c))+(c*(c>=a and c>=b))
min=(a*(a<=b and a<=c))+(b*(b<=a and b<=c))+(c*(c<=a and c<=b))
result=a+b+c-max-min
print("Result is ",result)

