'''Count Distinct Substrings (Rabin-Karp)
Count all distinct substrings of a string using Rabin-Karp algorithm and a dictionary.
Input: s = "abc"
Expected Output: 6'''

s=input("Enter the string:")
substrings = set()
for i in range(len(s)):
    for j in range(i, len(s)):
        substrings.add(s[i:j + 1])

    
print(len(substrings))
