''' The Dictionary of Two Kingdoms
The “North” kingdom and the “South” kingdom both keep ledgers of gold reserves. 
Suddenly, there’s a war—when they merge, the South’s gold value should overwrite the North’s 
wherever the city names match! What do the ledgers look like after the kingdoms unite?
Input: north = {'Winterfell': 1000, 'The Eyrie': 800}, south = {'The Eyrie': 1200, "King's Landing": 2500}
Expected Output: {'Winterfell': 1000, 'The Eyrie': 1200, "King's Landing": 2500}'''

import ast
N_kingdom=input("Enter the North kingdom details:")
N_kingdom=ast.literal_eval(N_kingdom)

S_kingdom=input("Enter the South kingdom details:")
S_kingdom=ast.literal_eval(S_kingdom)
N_kingdom.update(S_kingdom)
print("After kingdom reunite:",N_kingdom)
