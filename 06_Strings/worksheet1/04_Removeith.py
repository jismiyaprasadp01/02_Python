"""
Remove the i-th Character from a String
Explanation: Remove the character at a given index in a string (starting from 0).
Input: String = "Python", i = 2
"""
s=str(input("Enter the string"))
i=int(input("Enter the index"))
result=s[:i]+s[i+1:]
print(result)
