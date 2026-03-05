'''
Check for Pangram
Explanation: Verify if a string contains every letter of the alphabet at least once.'''

s = input("Enter the string: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in alphabet:
    if i not in s.lower():
        print("Not Pangram")
        break
else:
    print("Pangram")
