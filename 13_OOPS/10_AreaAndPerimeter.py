"""
All About Circles: Area and Perimeter
Scenario:
Designing a map app? You’ll want to know the area covered by a circular pond!

What you’ll learn:
Implementing methods with calculations
Understanding encapsulation

Task:
Build a Circle class with area() and perimeter() methods.

Example:
For a circle of radius 3:
Expected Output:
28.27
18.85
"""
import math
class Circle:
	def __init__(self,radius):
		self.radius=radius
	def area(self):
		return round(math.pi *self.radius **2,2)
	def perimeter(self):
		return round(2 *math.pi *self.radius,2)
c=Circle(2)
print(c.area())
print(c.perimeter())
