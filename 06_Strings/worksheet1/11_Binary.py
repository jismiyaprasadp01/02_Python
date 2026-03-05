"""
Check If a String is a Binary String
Explanation: Test if the string contains only '0' and '1'.
Input: "101101"
Expected Output: Is binary string: Yes
"""

s = input("Enter the string: ")
flag = True
for i in s:
    if i != '0' and i != '1':
        flag = False
        break

if flag:
    print("Is binary string: Yes")
else:
    print("Is binary string: No")
