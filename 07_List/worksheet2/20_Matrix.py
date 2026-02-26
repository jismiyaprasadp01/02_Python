"""
Task: Write a Python program to create a 3x3 matrix using nested list comprehensions.
Sample input: Rows: 3, Columns: 3
Output: [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
"""
a=int(input("Enter the no of rows"))
b=int(input("Enter the no of coloumns"))
matrix=[[i for j in range(b)] for i in range(a)]
print(matrix)
