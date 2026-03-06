"""
Python - Find missing and additional values in two lists
Story: You compared last week's and this week's homework lists. What's missing and what's new?
Sample Input:
old_hw = ["math", "science", "art"]
new_hw = ["math", "history", "science"]
Sample Output:
Missing: art
Additional: history
"""
a = ["math", "science", "art"]
b = ["math", "history", "science"]
missing=set(a)-set(b)
additional=set(b)-set(a)
print("Missing:", missing)
print("Additional:", additional)
