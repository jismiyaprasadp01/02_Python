"""
Check if a String is a Palindrome or Symmetrical
Explanation: A palindrome reads the same forwards and backwards (e.g., "madam"). A symmetrical string has matching halves.
Input: "madam"
Expected Output:
Palindrome: Yes
Symmetrical: Yes
"""
s=str(input("Enter the string"))
length=len(s)
is_palindrome=True
for i in range(length//2):
	if s[i]!=s[length-1-i]:
		is_palindrome=False
		break
if is_palindrome:
	print("Palindrome")
else:
	print("Not Palindrome")

	

