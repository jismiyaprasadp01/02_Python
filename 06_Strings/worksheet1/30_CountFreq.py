"""
Count Frequency of Words in String (Short Form)
Explanation: Show how many times each word appears.
Input: "apple apple orange"
Expected Output: {'apple': 2, 'orange': 1}
"""
text = "apple apple orange"
words = text.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print(freq)
