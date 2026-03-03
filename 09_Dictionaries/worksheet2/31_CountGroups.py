'''Count Groups by Digit Sum
Group numbers by the sum of their digits and report the size of the largest group.
Input: nums = [11, 20, 12, 21, 3]
Expected Output: 2'''

from collections import defaultdict
import ast
d=input("Enter the list:")
d=ast.literal_eval(d)
d1=defaultdict(list)
for num in d:
    sum1 =sum(int(i) for i in str(num))
    d1[sum1].append(num)
res = list(d1.values())
print(res)

print("output:",len(max(res,key=len)))
