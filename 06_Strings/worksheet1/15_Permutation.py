"""
Generate All Permutations of a String
Explanation: List all possible ways to rearrange the characters.
Input: "abc"
Expected Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
"""

from itertools import permutations
s = "abc"
result = []
for p in permutations(s):
    result.append(''.join(p))

print(result)
