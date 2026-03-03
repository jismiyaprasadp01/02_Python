"""
Find Close Matches for a String in a List
Explanation: Find list entries that are similar to the given word (helpful for typo correction).
Input: Target = "apple", List = ["apply", "apples", "ape", "maple"]
Expected Output: Close matches: ['apply', 'apples']
"""
import difflib

target = "apple"
words = ["apply", "apples", "ape", "maple"]

matches = difflib.get_close_matches(target, words, n=5, cutoff=0.6)

print("Close matches:", matches)
