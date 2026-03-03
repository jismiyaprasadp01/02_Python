"""
Family Traits: Inheritance in Action with Vehicles and Buses
Scenario:
You’re modeling a transportation system. Buses are vehicles, so shouldn’t they share common features?

What you’ll learn:
Inheriting attributes and methods from a parent class
The principle of code reuse and extension

Task:
Log Session a Vehicle class and a Bus class that inherits from it. Demonstrate shared behavior.

Example:
Suppose you make a Bus object and call its move() method.

http://192.168.2.101/link/421#bkmrk-expected-output%3A-2
 
Expected Output:
Vehicle is moving
"""
class Vehicle:
	def move(self):
		print("Vehicle is Moving\n")
class Bus(Vehicle):
	pass
my_bus=Bus()
my_bus.move()
