"""
Shape Shifters: Mastering Class Inheritance
Scenario:
Imagine you’re building a drawing tool. You have a general Shape, but want to specialize it into Circle and Square.

What you’ll learn:
The basics of inheritance
How subclasses can extend or override parent class functionality

Task:
Log Session a Shape class with a method called draw(). Inherit and customize in Circle and Square.

Example:
If you create a Circle and ask it to draw():

http://192.168.2.101/link/421#bkmrk-expected-output%3A-3
 
Expected Output:
Drawing a circle
"""
class Shape:
	def draw(self):
		print("Drawing a shape")
class Circle(Shape):
	def draw(self):
		print("Drawing a Circle")
class Square(Shape):
	def draw(self):
		print("Drawing a Square")
c=Circle()
s=Square()
c.draw()
s.draw()
