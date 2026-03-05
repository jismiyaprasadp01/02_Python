"""
Check if a String is a Palindrome or Symmetrical
Explanation: A palindrome reads the same forwards and backwards (e.g., "madam"). A symmetrical string has matching halves.
Input: "madam"
Expected Output:
Palindrome: Yes
Symmetrical: Yes
"""
s = "madam"
if s== s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
