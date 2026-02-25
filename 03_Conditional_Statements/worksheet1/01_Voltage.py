"""
Given a voltage reading, print "Under Voltage", "Nominal", or "Over Voltage".
(Nominal is between 3.0V and 3.3V inclusive.)
Input: 3.35
Output: Over Voltage
"""
voltage = float(input("Enter the voltage: "))

if 3.0 <= voltage <= 3.3:
    print("Nominal")
elif voltage < 3.0:
    print("Under Voltage")
else:
    print("Over Voltage")
