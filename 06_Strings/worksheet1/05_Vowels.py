"""
Count Vowels in a String Using Sets
Explanation: Find how many vowels (a, e, i, o, u) are in the string, using sets for efficiency.
Input: "education"
Expected Output: Vowels Count: 5
"""
s=str(input("Enter the string"))
vowels={'a','e','i','o','u'}
count=0
for i in s.lower():
	if i in vowels:
		count+=1
print("vowels count:",count)
