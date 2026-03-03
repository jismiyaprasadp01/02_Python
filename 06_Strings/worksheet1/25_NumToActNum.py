"""
Convert Numeric Words to Actual Numbers
Explanation: Replace words like 'one', 'two' with their numeric equivalents.
Input: "I have one apple and two oranges."
Expected Output: "I have 1 apple and 2 oranges."
"""
import re

word_to_num = {
    "zero": "0", "one": "1", "two": "2", "three": "3",
    "four": "4", "five": "5", "six": "6",
    "seven": "7", "eight": "8", "nine": "9", "ten": "10"
}

def replace(match):
    return word_to_num[match.group(0).lower()]

text = "I have one apple and two oranges."
pattern = re.compile(r'\b(' + '|'.join(word_to_num.keys()) + r')\b', re.IGNORECASE)

print(pattern.sub(replace, text))
