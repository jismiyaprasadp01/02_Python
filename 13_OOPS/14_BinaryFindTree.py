"""
Binary Find Tree: Smart Organization
Scenario:
Organize data for fast searching, like contacts or scores.

What you’ll learn:
Implementing data structures as classes
Recursion in OOP

Task:
Build a BST class with methods for insertion and search.

Example:
Insert numbers and search for 5.

Expected Output:
True or False (depending on search)
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current, value):
        if current is None:
            return False
        if value == current.value:
            return True
        elif value < current.value:
            return self._search_recursive(current.left, value)
        else:
            return self._search_recursive(current.right, value)

tree = BST()

numbers = [8, 3, 10, 1, 6, 14, 5]
for num in numbers:
    tree.insert(num)

print(tree.search(5)) 
print(tree.search(20)) 
