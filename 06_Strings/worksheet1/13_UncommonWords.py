"""
Find Uncommon Words Between Two Strings
Explanation: List words present in only one of the two strings.
Input: "red blue green", "blue yellow red"
Expected Output: Uncommon words: ['green', 'yellow']
"""
s1 = "red blue green"
s2 = "blue yellow red"
set1 = set(s1.split())
set2 = set(s2.split())
uncommon = list(set1.symmetric_difference(set2))
print("Uncommon words:", uncommon)
