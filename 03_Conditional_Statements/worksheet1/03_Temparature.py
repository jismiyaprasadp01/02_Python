"""
Enter a temperature and print "Overheat" (>75°C), "Normal" (25-75°C), or "Low Temp" (<25°C).
Input: 18
Output: Low Temp
"""
temp=int(input("Enter the temparature"))
if temp<25:
	print("Low Temp")
elif temp>75:
	print("Overheat")
else :
	print("Normal")
