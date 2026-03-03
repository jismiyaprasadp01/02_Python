"""
One for All: The Magic of Class Attributes
Scenario:
All students in a school belong to the same institution. How can you ensure this is reflected in every student object?

What you’ll learn:
Class (static) attributes: properties shared by all instances
When and why to use them

Task:
Define a Student class where every student has the same school_name.

Example:
If you create two students and print their school_name:

Expected Output:
Central High School Central High School
"""
class Student:
	school_name="Army School"
	def __init__(self,name):
		self.name=name
s1=Student("jismiya")
s2=Student("prasad")
print(s1.school_name,s2.school_name)

