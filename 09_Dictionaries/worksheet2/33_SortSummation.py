'''Sort by Values Summation
Sort a dictionary by the sum of its list values, from smallest to largest.
Input: d = {'x': [5,5], 'y': [1,2,3], 'z': [10]}
Expected Output: [('y', [1,2,3]), ('x', [5,5]), ('z', [10])]'''

import ast
d=input("Enter the dictionary:")
d=ast.literal_eval(d)

sorted_list=sorted(d.items(),key=lambda x: sum(x[1]))

print(sorted_list)
