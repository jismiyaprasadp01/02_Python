'''
 Task 1: Word Count Script
 Covers: Basic syntax, data types, and file I/O
 Description: Read a text file, count the frequency of each word, and output the results as a 
dictionary.
'''


from collections import defaultdict

with open('word.txt', 'r') as file:
    inp = file.read()

words = inp.split()
freq = defaultdict(int)

for word in words:
    freq[word] += 1

print(dict(freq))

