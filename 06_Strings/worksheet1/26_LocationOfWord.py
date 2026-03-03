"""
Find the Location of a Word in a String
Explanation: Find the index where a word first appears in the string.
Input: String = "welcome to python", Word = "python"
Expected Output: Position: 11
"""
text = "welcome to python"
word = "python"
position = text.find(word)
if position != -1:
    print(f"Position: {position}")
else:
    print("Word not found")
