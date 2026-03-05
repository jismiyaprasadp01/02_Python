"""
Generate Random Strings Until a Target String is Formed
Explanation: Keep generating random strings until you produce the target string.
Input: Target = "abc"
Expected Output: Randomly generated 'abc' after N attempts (N will vary)
"""
import random

target = "abc"
attempts = 0

while True:
    s = ""
    for i in range(len(target)):
        s = s + random.choice("abcdefghijklmnopqrstuvwxyz")

    attempts += 1

    if s == target:
        print("Found:", s)
        print("Attempts:", attempts)
        break
