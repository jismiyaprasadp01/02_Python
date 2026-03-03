''' Pairing the Guest List
You have two lists: guest names and their seat numbers. Match each guest to their seat for the dinner plan!
Input: names = ['Alice', 'Bob', 'Eve'], seats = [5, 12, 8]
Expected Output: {'Alice': 5, 'Bob': 12, 'Eve': 8}'''

import ast
list1=input("Enter the guest list:")
list1=ast.literal_eval(list1)
list2=input("Enter the seat numbers list:")
list2=ast.literal_eval(list2)
d=zip(list1,list2)
print(dict(d))
