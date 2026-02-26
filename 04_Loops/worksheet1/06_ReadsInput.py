"""
Check if the input number reads the same backward as forward, using only loops and arithmetic
"""
num=int(input("Enter the number"))
temp=num
rev=0
while temp>0:
 r=temp%10
 rev=rev*10+r
 temp=temp//10
if num==rev:
 print("Palindrome")
else:
 print("Not Palindrome")
