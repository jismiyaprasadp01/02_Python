"""
Rotate a String by k Positions
Explanation: Shift characters in the string to the right by k positions.
Input: String = "hello", k = 2
Expected Output: "lohel"
"""
s = "hello"
k = 2

k = k % len(s)
rotated = s[-k:] + s[:-k]

print(rotated)
