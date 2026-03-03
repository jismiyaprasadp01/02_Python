"""
Scenario:
Log Session a feature like "undo" in a drawing app.

What you’ll learn:
How to build a stack (LIFO) using classes
Using lists for stack operations

Task:
Implement a Stack class with push and pop methods.

Example:
Push 10, then 20; pop an element.
Expected Output:
20
"""
class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.items:
            return "Stack is empty"
        return self.items.pop()


s = Stack()

s.push(10)
s.push(20)

print(s.pop())
