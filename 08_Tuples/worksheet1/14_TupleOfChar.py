"""
Description: Convert a tuple of characters to a string and then back to a tuple.
Useful for text manipulation and transitioning between data representations.
Input: t = ('P', 'y', 't', 'h', 'o', 'n')
Output: String: "Python"
Tuple: ('P', 'y', 't', 'h', 'o', 'n')
"""
t = ('P', 'y', 't', 'h', 'o', 'n')
a = "".join(t)
b= tuple(a)
print("String: a)
print("Tuple:", b)
