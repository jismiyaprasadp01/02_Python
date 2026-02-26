"""
Find the Maximum Frequency Character
Explanation: Determine which character appears most frequently in the string.
Input: "banana"
Expected Output: Maximum frequency character: 'a'
"""
s=str(input("Enter the string"))
freq={}
for i in s:
	if i in freq:
		freq[i]+=1
	else:
		freq[i]=1
max_count=max(freq.values())
for i in s:
	if freq[i]==max_count:
		print("Maximum frequent chracater :",i)
		freq[i]=0
		
