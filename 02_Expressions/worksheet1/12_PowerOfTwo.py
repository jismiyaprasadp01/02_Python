"""
Check if a Number is a Power of Two
Write a single Boolean expression to check if a number is a power of two.
Sample Input: n = 32

"""
num=int(input("Enter the num"))
if (num>0 and num&(num-1)==0):
 print("power of two")
else:
 print("Not a power of two")
