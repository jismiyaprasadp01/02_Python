"""
Frequency of Consecutive Characters
Explanation: Count how many times each character repeats in sequence.
Input: "aabccddd"
Expected Output: {'a': 2, 'b': 1, 'c': 2, 'd': 3}
"""

s = "aabccddd"
result = {}
count = 1
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        result[s[i-1]] = count
        count = 1

result[s[-1]] = count

print(result)
