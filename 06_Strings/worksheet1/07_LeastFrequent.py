"""
Identify the Least Frequent Character in a String
Explanation: Find the character(s) that occur(s) the fewest times in a string.
Input: "statistics"
Expected Output: Least frequent character: 'a'
"""
s = input("Enter the string: ")

freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

min_count = min(freq.values())

for ch in freq:
    if freq[ch] == min_count:
        print("Least frequent character:", ch)
