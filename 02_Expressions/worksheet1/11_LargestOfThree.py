"""
Find the Largest of Three Numbers Using Only Expressions
Without using if, elif, or any function, write an expression to find the largest of three given numbers.
Sample Input: a = 14, b = 27, c = 19
"""
a,b,c=map(int,input("Enter a b c").split())
largest=(a*(a>=b and a>=c)+b*(b>=a and b>=c)+c*(c>=a and c>=b))
print("Largest is :",largest)
