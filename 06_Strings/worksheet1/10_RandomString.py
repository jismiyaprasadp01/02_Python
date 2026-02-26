"""
Generate Random Strings Until a Target String is Formed
Explanation: Keep generating random strings until you produce the target string.
Input: Target = "abc"
Expected Output: Randomly generated 'abc' after N attempts (N will vary)"""
import random

target = input("Enter target string: ")
attempts = 0
letters = "abckkkkkkkkkkkkkkkkkkkkkk"

while True:
    attempts += 1
    generated = ""

    for i in range(len(target)):
        generated += random.choice(letters)

    if generated == target:
        print("Generated:", generated)
        print("Attempts:", attempts)
        break
