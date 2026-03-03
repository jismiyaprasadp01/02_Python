'''
Convert Snake Case to Pascal Case
Explanation: Change a snake_case string (words separated by underscores) into PascalCase (words start with uppercase, no underscores).
'''

def snake_to_pascal(s):
    parts = s.split('_')
    pascal_str = ''.join(word.capitalize() for word in parts)
    return pascal_str

s = input("Enter the string: ")
output_str = snake_to_pascal(s)
print(output_str)
