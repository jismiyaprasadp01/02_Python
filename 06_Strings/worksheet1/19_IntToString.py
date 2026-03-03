"""
Convert Integer to String and Vice Versa
Explanation: Change a number to a string, and a string of digits to an integer.
Input: Integer = 123, String = "456"
Expected Output:
Integer to string: '123'
String to integer: 456
"""
num = 123
text = "456"

num_to_string = str(num)
string_to_num = int(text)

print(f"Integer to string: '{num_to_string}'")
print(f"String to integer: {string_to_num}")
