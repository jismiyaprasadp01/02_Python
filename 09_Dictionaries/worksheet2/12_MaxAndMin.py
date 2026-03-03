'''Max and Min Detective
Among all your valuables (dictionary values), who owns the largest and smallest? Report both the max and min key names.
Input: valuables = {'ring': 5, 'necklace': 9, 'watch': 2}
Expected Output: Max: 'necklace', Min: 'watch' '''

import ast
valuables=input("Enter the valuables details:")
valuables=ast.literal_eval(valuables)

print("max:",max(valuables,key=valuables.get),"min:",min(valuables,key=valuables.get))
