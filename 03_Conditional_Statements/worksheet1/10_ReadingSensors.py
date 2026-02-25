"""
Given three sensor readings, print "Majority High" if at least two readings are above a threshold (e.g., 50), otherwise "Majority Low".
Input: 40, 65, 70
Output: Majority High
"""
a, b, c = map(int, input("Enter three sensor readings: ").split())

threshold = 50

count_high = (a > threshold) + (b > threshold) + (c > threshold)

if count_high >= 2:
    print("Majority High")
else:
    print("Majority Low")
