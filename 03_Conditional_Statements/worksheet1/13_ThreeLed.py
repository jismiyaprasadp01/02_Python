"""
Given the status of three LEDs (on/off as 1/0), print which LEDs are ON. If all are off, print "All LEDs off".
Input: 0, 1, 0
Output: LED2 ON
"""
led1, led2, led3 = map(int, input("Enter LED1 LED2 LED3 (0/1): ").split())

if led1 == 0 and led2 == 0 and led3 == 0:
    print("All LEDs off")
else:
    if led1:
        print("LED1 ON")
    if led2:
        print("LED2 ON")
    if led3:
        print("LED3 ON")
