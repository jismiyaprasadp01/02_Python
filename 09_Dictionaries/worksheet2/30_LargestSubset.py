'''Largest Subset of Anagram Words
Given a list of words, find the size of the largest subset where all are anagrams of each other.
Input: words = ['bat', 'tab', 'eat', 'tea', 'tan', 'nat']
Expected Output: 3'''

from collections import defaultdict
import ast
d=input("Enter the list:")
d=ast.literal_eval(d)
d1=defaultdict(list)
for word in d:
    sort_word = ''.join(sorted(word))
    d1[sort_word].append(word)
    

res = list(d1.values())
max=0
list=[]
for i in res:
    if len(i)>max:
        max=len(i)
        list=i
print("The largest one:",list,'length',max)
