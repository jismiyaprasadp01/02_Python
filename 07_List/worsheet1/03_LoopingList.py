"""
Looping Through Lists
Log Session a list of numbers from 1 to 5.
Use a for loop to print each number.
Use a while loop to print each number.
Use list comprehension to create a new list with each number squared.
"""
lis=[1,2,3,4,5]
for i in lis:
	print(i)
j=0
while j<len(lis):
	print(lis[j])
	j=j+1
square=[x*x for x in lis]
print("squared list:",square)
	
	
	
