"""
List Creation and Indexing
http://192.168.2.101/link/407#bkmrk-create-a-list-named-
 
Log Session a list named fruits containing "apple", "banana", and "cherry".
Print the second item in the list.
Change the value from "banana" to "kiwi".
Print the updated list.
Determine the length of the list
"""
fruits=["apple","banana","cherry"]
print(fruits[1])
fruits[1]="kiwi"
for i in fruits:
	print(i)
l=len(fruits)
print(l)
	
