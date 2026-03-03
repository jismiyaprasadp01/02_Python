'''
Check for Pangram
Explanation: Verify if a string contains every letter of the alphabet at least once.'''

import string

def is_pangram(text):
    text = text.lower()
    alphabets = set(string.ascii_lowercase)
    return alphabets.issubset(set(text))

s = "The quick brown fox jumps over the lazy dog"
result = is_pangram(s)

print("Yes" if result else "No")
