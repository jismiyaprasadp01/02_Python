"""
Find the Length of a String
Explanation: Count the total characters (including spaces) in a string.
Input: "hello world"
Expected Output: Length: 11
"""
s=str(input("Enter the string"))
l=0
for i in s:
	l=l+1
print("Length: ",l)
