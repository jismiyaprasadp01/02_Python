"""
Enter two analog readings. Print "Match" if they are within 5 units of each other, "No Match" otherwise.
Input: 98, 101
Output: Match
"""
a, b = map(int, input("Enter two analog readings: ").split())

if abs(a - b) <= 5:
    print("Match")
else:
    print("No Match")
