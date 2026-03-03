"""
Are You One of Us? Checking Class Membership
Scenario:
You want to make sure a Bus object can access special parking. But only if it’s really a Vehicle.

What you’ll learn:
Using isinstance() to check an object’s class or parent classes
Dynamic type safety

Task:
Check if a Bus object is an instance of Vehicle.

Example:
You check with isinstance() for a Bus object.

http://192.168.2.101/link/421#bkmrk-expected-output%3A-6
 
Expected Output
True
"""
class Vehicle:
	pass
class Bus(Vehicle):
	pass
my_bus=Bus()
print(isinstance(my_bus,Vehicle))
