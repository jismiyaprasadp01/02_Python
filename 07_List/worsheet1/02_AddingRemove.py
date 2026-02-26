"""
Adding and Removing Items
http://192.168.2.101/link/407#bkmrk-append-%22orange%22-to-t
 
Append "orange" to the fruits list.
Insert "mango" at the second position.
Remove "apple" from the list.
Use the pop() method to remove the last item.
Clear the entire list.
"""
fruits=["apple","kiwi","banana"]
fruits.append("orange")
fruits.insert(1,"mango")
fruits.remove("apple")
fruits.pop()
fruits.clear()
print(fruits)

