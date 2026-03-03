"""
Queue It Up: Fair Turn for All
Scenario:
Manage waiting lines—like people in a ticket queue.

What you’ll learn:
Implementing a queue (FIFO) in Python
Real-world queue management

Task:
Build a Queue class with enqueue and dequeue methods.

Example:
Enqueue 10, then 20; dequeue once.

http://192.168.2.101/link/421#bkmrk-expected-output%3A-18
 
Expected Output:
10
"""
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if not self.items:
            return "Queue is empty"
        return self.items.pop(0)


q = Queue()

q.enqueue(10)
q.enqueue(20)

print(q.dequeue())
