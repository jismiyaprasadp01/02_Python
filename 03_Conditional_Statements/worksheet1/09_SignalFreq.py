"""
Enter a signal frequency (Hz). Print "Low Band" (<1000), "Mid Band" (1000–9999), "High Band" (10000–99999), or "Out of Range".
Input: 8000
Output: Mid Band
"""
freq = int(input("Enter signal frequency (Hz): "))

if freq < 0:
    print("Out of Range")
elif freq < 1000:
    print("Low Band")
elif freq <= 9999:
    print("Mid Band")
elif freq <= 99999:
    print("High Band")
else:
    print("Out of Range")
