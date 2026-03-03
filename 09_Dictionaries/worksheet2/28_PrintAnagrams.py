'''Print Anagrams Together Using List and Dictionary
Group words that are anagrams together from a list (all the jumbled twins in one basket).
Input: words = ['listen', 'silent', 'enlist', 'hello', 'ohlle']
Expected Output: [['listen', 'silent', 'enlist'], ['hello', 'ohlle']]'''
from collections import defaultdict
import ast
d=input("Enter the list:")
d=ast.literal_eval(d)
d1=defaultdict(list)
for word in d:
    sort_word = ''.join(sorted(word))
    d1[sort_word].append(word)
    

res = list(d1.values())
print(res)
    
