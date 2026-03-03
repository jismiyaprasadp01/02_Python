"""
Description: Compute the frequency of each element in a tuple and return the result as a dictionary.
Element frequency counting is widely used for data summarization, analytics, and validation tasks.
Input: t = (1, 2, 2, 3, 3, 3)
Output: {1: 1, 2: 2, 3: 3}
"""
t = (1, 2, 2, 3, 3, 3)
freq = {}
for item in t:
    freq[item] = freq.get(item, 0) + 1
print(freq)
