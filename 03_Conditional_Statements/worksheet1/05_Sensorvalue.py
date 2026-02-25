"""
If a sensor value is outside the range 100–900, print "Sensor Fault". If within, print "Sensor OK".
Input: 950
Output: Sensor Fault
"""
sensor = int(input("Enter sensor value: "))

if sensor < 100 or sensor > 900:
    print("Sensor Fault")
else:
    print("Sensor OK")
