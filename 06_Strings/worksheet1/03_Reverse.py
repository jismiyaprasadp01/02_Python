"""
Reverse Words in a String
Explanation: Reverse the order of words in a sentence, not the letters.
Input: "I love Python"
Expected Output: "Python love I"
"""
s = input("Enter the string: ")

words = s.split()

for i in range(len(words) - 1, -1, -1):
    print(words[i], end=" ")
