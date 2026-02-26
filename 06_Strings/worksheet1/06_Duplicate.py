"""Eliminate Duplicate Characters from a String
Explanation: Log Session a new string containing only the first occurrence of each character.
Input: "programming"
Expected Output: "progamin
"""
s = input("Enter the string: ")

result = ""
seen = set()

for i in s:
    if i not in seen:
        result = result + i
        seen.add(i)

print(result)
