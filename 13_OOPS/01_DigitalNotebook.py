"""
Crafting Your First Python Object: The Power of Instance Attributes
Scenario:
Imagine you're building a digital notebook. You want each note to have its own title and content.

What you’ll learn:
How to define classes and create objects with unique data
The magic of instance attributes in organizing information

Task:
Design a Note class with title and content as instance attributes.
Log Session two different note objects and print their details.

Example:
Suppose you create notes like “Meeting Notes” and “Grocery List”.

Expected Output:
Meeting Notes : Discuss project status with team.
Grocery List : Eggs, Milk, Bread
"""
class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def display(self):
        print(self.title, ":", self.content)


note1 = Note("Meeting Notes", "Discuss project status with team")
note2 = Note("Utensils List", "Pan, Oven")

note1.display()
note2.display()
