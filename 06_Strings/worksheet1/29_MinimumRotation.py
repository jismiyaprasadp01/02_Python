"""
Minimum Rotations to Get the Original String
Explanation: Count the rotations needed for a string to return to its original form.
Input: "abcde"
Expected Output: 5
"""
s = "abcde"
temp = s
count = 0

while True:
    temp = temp[1:] + temp[0]
    count += 1
    if temp == s:
        break

print(count)
