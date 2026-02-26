"""
Sorting and Copying Lists
http://192.168.2.101/link/407#bkmrk-create-a-list-of-num-1
 
Log Session a list of numbers: [3, 1, 4, 2, 5].
Sort the list in ascending order.
Sort the list in descending order.
Copy the sorted list to a new list.
Print both lists to verify they are separate copies.
"""
numbers = [3, 1, 4, 2, 5]

numbers.sort()
print("Ascending:", numbers)

numbers.sort(reverse=True)
print("Descending:", numbers)

copied_list = numbers.copy()

print("Original list:", numbers)
print("Copied list:", copied_list)
