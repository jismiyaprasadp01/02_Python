"""
Identify the Least Frequent Character in a String
Explanation: Find the character(s) that occur(s) the fewest times in a string.
Input: "statistics"
Expected Output: Least frequent character: 'a'
"""
s = input("Enter the string: ")
min_char = min(s, key=s.count)
print("Maximum frequency character:", min_char)
