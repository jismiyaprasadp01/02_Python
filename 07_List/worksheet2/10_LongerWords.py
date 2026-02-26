"""
Task: Write a Python program to find the list of words that are longer than n from a given list of words.
Sample input: ['hello', 'world', 'python', 'is', 'great'], n = 4
Output: ['hello', 'world', 'python', 'great']
"""
a=['hello', 'world', 'python', 'is', 'great']
n=4
result=[]
for i in a:
	if len(i)>4:
		result.append(i)
print(result)
