#Remove Punctuation from a String

import string

def remove_punctuation(text):
    return ''.join(char for char in text if char.isalnum() or char.isspace())

s = "Hello, world! How are you?"
output = remove_punctuation(s)
print(output)
