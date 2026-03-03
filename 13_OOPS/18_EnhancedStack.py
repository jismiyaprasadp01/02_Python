"""
Enhanced Stack: Show Me What’s Inside
Scenario:
See the current state of the stack—great for debugging.

What you’ll learn:
Extending existing classes
Useful methods for state visibility

Task:
Add a display method to your Stack class to show its elements.

Example:
Push 1, then 2; display stack.

http://192.168.2.101/link/421#bkmrk-expected-output%3A-17
 
Expected Output:
[1, 2]
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

    def display(self):
        print(self.items)


s = Stack()

s.push(1)
s.push(2)

s.display()
