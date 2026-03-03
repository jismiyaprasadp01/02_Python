"""
Description: Identify and print elements that occur more than once in a tuple.
Spotting duplicates in sequences is common in data cleaning and interviews.
Input: t = (2, 4, 6, 2, 8, 4, 6, 2)
Output: 2, 4, 6
"""
t = (2, 4, 6, 2, 8, 4, 6, 2)
duplicates = []
for item in t:
    if t.count(item) > 1 and item not in duplicates:
        duplicates.append(item)
print(*duplicates)
