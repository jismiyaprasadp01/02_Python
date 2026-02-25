"""
Accept a device mode value:
- 0: "Standby"
- 1: "Active"
- 2: "Fault"
- Any other: "Unknown mode"
"""
led1, led2, led3 = map(int, input("Enter LED1 LED2 LED3 (0/1): ").split())

if not (led1 or led2 or led3):
    print("All LEDs off")
else:
    if led1: print("LED1 ON")
    if led2: print("LED2 ON")
    if led3: print("LED3 ON")
