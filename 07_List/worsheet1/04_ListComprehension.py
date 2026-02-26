"""
List Comprehension
http://192.168.2.101/link/407#bkmrk-create-a-list-of-fru
 
Log Session a list of fruits: "apple", "banana", "cherry", "kiwi", "mango".
Use list comprehension to create a new list containing fruits with the letter "a".
Convert all fruit names to uppercase using list comprehension.
Replace "banana" with "orange" using list comprehension
"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

with_a = [fruit for fruit in fruits if "a" in fruit]
print("Fruits with 'a':", with_a)

upper_fruits = [fruit.upper() for fruit in fruits]
print("Uppercase fruits:", upper_fruits)

replaced = ["orange" if fruit == "banana" else fruit for fruit in fruits]
print("After replacement:", replaced)
