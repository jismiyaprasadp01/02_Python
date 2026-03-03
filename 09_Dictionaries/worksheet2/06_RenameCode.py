'''Secret Spy Codes
You intercepted a list of coded messages (keys), but your team uses new code names (a mapping). 
How will you quickly rename every code to its new secret label?
Input: codes = {'alpha': 'ok', 'beta': 'wait'}, new_labels = {'alpha': 'red', 'beta': 'blue'}
Expected Output: {'red': 'ok', 'blue': 'wait'}'''

import ast
codes=input("Enter the code details:")
codes=ast.literal_eval(codes)

new_labels=input("Enter the label details:")
new_labels=ast.literal_eval(new_labels)

translated = {new_labels[code]: status for code, status in codes.items()}

print("Output:",translated)
