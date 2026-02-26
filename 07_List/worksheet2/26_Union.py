"""
Task: Write a Python function to find the union and intersection of two lists.
Sample input: [1, 2, 3, 4], [3, 4, 5, 6]
Output: Union: [1, 2, 3, 4, 5, 6]
Intersection: [3, 4]
"""
def union_intersection(a, b):
    union = list(set(a) | set(b))
    intersection = list(set(a) & set(b))
    return union, intersection

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

u, i = union_intersection(a, b)
print("Union:", u)
print("Intersection:", i)
