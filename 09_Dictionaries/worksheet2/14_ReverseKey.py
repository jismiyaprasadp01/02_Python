'''Value to Key Reverse Find
You know a value, but not which key owns it. Trace back and report the key for a given value!
Input: d = {'x': 100, 'y': 200}, value = 200
Expected Output: Key for value 200: 'y' '''

import ast
d=input("Enter the dictionary details:")
d=ast.literal_eval(d)
s = int(input("Enter the value to search for key:"))

for i,k in d.items():
    if k==s:
        print("Output:key for value",k,'is',i)
        break
else:
    print("value is not present")
