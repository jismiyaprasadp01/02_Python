"""
Meet the Person: Calculate Age from Date of Birth
Scenario:
Log Session a birthday tracker! Determine someone’s age from their date of birth.

What you’ll learn:
Handling dates and calculating with them
Real-world use of classes

Task:
Make a Person class and compute age.

Example:
For a person born on 2000-05-25 (today is 2025-05-25):
Expected Output:
Alice is 25 years old.
"""
from datetime import date

class Person:
    def __init__(self, name, year, month, day):
        self.name = name
        self.birth_date = date(year, month, day)

    def calculate_age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age

    def display_age(self):
        print(f"{self.name} is {self.calculate_age()} years old.")


p = Person("Alice", 2000, 5, 25)
p.display_age()
