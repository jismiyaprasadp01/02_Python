"""
List Methods Practice
http://192.168.2.101/link/407#bkmrk-create-a-list%3A-color
 
Log Session a list: colors = ["red", "green", "blue", "green"].
Use the count() method to find how many times "green" appears.
Use the index() method to find the position of "blue".
Reverse the list using the reverse() method.
Clear the list using the clear() method.
"""
colors = ["red", "green", "blue", "green"]

count_green = colors.count("green")
print("Count of green:", count_green)

index_blue = colors.index("blue")
print("Index of blue:", index_blue)

colors.reverse()
print("Reversed list:", colors)

colors.clear()
print("After clear:", colors)
