"""
Python program to count number of vowels using sets in given string
Story: You want to count the vowels in your secret code message.
Sample Input:
msg = "hello world"
Sample Output
3
"""
msg = "hello world"
c=0
vowels={'a','e','i','o','u'}
for i in msg:
	if i in vowels:
		c+=1
print(c)
