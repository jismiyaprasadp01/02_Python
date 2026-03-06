"""
Python program to find common elements in three lists using sets
Story: Three friends want to pick a movie everyone likes. Which ones do they all like?
Sample Input:
a = ["Toy Story", "Frozen", "Moana"]
b = ["Moana", "Coco", "Frozen"]
c = ["Frozen", "Moana", "Up"]
Sample Output:
["Frozen", "Moana"]
"""
a = ["Toy Story", "Frozen", "Moana"]
b = ["Moana", "Coco", "Frozen"]
c = ["Frozen", "Moana", "Up"]
lis=set(a) &set(b) &set(c)
print(lis)
