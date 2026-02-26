"""
Joining and Extending Lists
http://192.168.2.101/link/407#bkmrk-create-two-lists%3A-li
 
Log Session two lists: list1 = ["a", "b", "c"] and list2 = [1, 2, 3].
Concatenate the two lists into a new list.
Use the extend() method to add list2 to list1.
Print the final lists.
"""
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

new_list = list1 + list2
print("Concatenated list:", new_list)

list1.extend(list2)
print("After extend list1:", list1)
print("list2 remains:", list2)
