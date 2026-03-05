"""
Convert Numeric Words to Actual Numbers
Explanation: Replace words like 'one', 'two' with their numeric equivalents.
Input: "I have one apple and two oranges."
Expected Output: "I have 1 apple and 2 oranges."
"""
text = "I have one apple and two oranges"

d = {
    "zero":"0",
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9"
}

words = text.split()

result = []

for w in words:
    if w in d:
        result.append(d[w])
    else:
        result.append(w)

print(" ".join(result))
