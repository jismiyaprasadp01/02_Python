"""
The Linked List: Chain Reaction
Scenario:
Store and process data efficiently, like songs in a playlist.

What you’ll learn:
Building a linked list from scratch
Understanding nodes and pointers

Task:
Write a LinkedList class with insert, delete, and display.

Example:
Add 10, then 20, and display list.
Expected Output:
10 -> 20
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def delete(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> " if temp.next else "")
            temp = temp.next
        print()


ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.display()
