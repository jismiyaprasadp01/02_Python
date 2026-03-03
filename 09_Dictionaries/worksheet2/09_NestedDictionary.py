'''Update the Employee Profile
A nested dictionary holds employee info. An employee changed their phone number. 
Update it without touching the rest of their info.
Input: profile = {'info': {'name': 'Sam', 'phone': '555-1234'}}, new_phone = '555-9999'
Expected Output: {'info': {'name': 'Sam', 'phone': '555-9999'}}'''
import ast
profile=input("Enter the employees details:")
profile=ast.literal_eval(profile)
n=input("Enter whose profile you want to update:")
s=input("Enter the update phone number:")

for i,j in profile.items():
    if j['name'] ==n:
        j['phone']=s
print(profile)
