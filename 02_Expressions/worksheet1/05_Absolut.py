"""
Get the Absolute Value
Write an expression to get the absolute value of a number.
Sample Input: n = -12
"""
num=int(input("Enter num"))
#a=abs(num)
a=num if num>=0 else -num
print("Absolute value is ",a)
