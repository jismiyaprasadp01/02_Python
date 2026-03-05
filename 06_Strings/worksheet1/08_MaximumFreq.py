"""
Find the Maximum Frequency Character
Explanation: Determine which character appears most frequently in the string.
Input: "banana"
Expected Output: Maximum frequency character: 'a'
"""
s = input("Enter the string: ")

max_char = max(s, key=s.count)

print("Maximum frequency character:", max_char)
