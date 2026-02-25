"""
Given a digital input value (0–255), determine and print which of 4 quadrants it falls into:
- 0–63, 64–127, 128–191, 192–255
"""
value = int(input("Enter digital value (0–255): "))

if 0 <= value <= 63:
    print("Quadrant 1 (0–63)")
elif 64 <= value <= 127:
    print("Quadrant 2 (64–127)")
elif 128 <= value <= 191:
    print("Quadrant 3 (128–191)")
elif 192 <= value <= 255:
    print("Quadrant 4 (192–255)")
else:
    print("Invalid Input")
