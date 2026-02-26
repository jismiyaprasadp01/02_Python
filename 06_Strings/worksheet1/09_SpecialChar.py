"""
if a String Contains Special Characters
Explanation: Check if the string contains characters other than letters or numbers.
Input: "Hello@123"
Expected Output: Contains special character: Yes
"""
s=str(input("Enter the string"))
found=False
for i in s:
	if not i.isalnum():
		found=True
		break
if found:
		print("yes")
else:
		print("no")
