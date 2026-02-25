"""
Given three boolean flags: `power_on`, `overcurrent`, `overvoltage`, print:
- "System Safe" if only `power_on` is True.
- "Shut Down: Overcurrent" if `overcurrent` is True.
- "Shut Down: Overvoltage" if `overvoltage` is True.
- "Critical Failure" if both faults are True.
Input: True, True, False
Output: Shut Down: Overcurrent
"""
power_on, overcurrent, overvoltage = map(
    lambda x: x == "True",
    input("Enter power_on overcurrent overvoltage (True/False): ").split()
)

if overcurrent and overvoltage:
    print("Critical Failure")
elif overcurrent:
    print("Shut Down: Overcurrent")
elif overvoltage:
    print("Shut Down: Overvoltage")
elif power_on:
    print("System Safe")
else:
    print("System Off")
