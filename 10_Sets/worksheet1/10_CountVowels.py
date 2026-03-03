'''Python program to c number of vowels using sets in given string
Vowels can be put in a set for quick checking!'''
def count_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    c = 0
    for char in s.lower():
        if char in vowels:
            c += 1
    return c

s = input("Enter the string:")
print("Number of vowels:", count_vowels(s))
