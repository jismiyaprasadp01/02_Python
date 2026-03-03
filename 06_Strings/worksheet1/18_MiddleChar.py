"""
Print the Middle Character of a String
Explanation: Display the character(s) at the center of the string.
Input: "python"
Expected Output: Middle character: 't' and 'h'
"""
s = "python"
length = len(s)
if length % 2 == 0:
    mid1 = s[length//2 - 1]
    mid2 = s[length//2]
    print(f"Middle characters: '{mid1}' and '{mid2}'")
else:
    mid = s[length//2]
    print(f"Middle character: '{mid}'")
