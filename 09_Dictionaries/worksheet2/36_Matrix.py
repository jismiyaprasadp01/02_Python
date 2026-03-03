''' Scoring Matrix Using Dictionary
Build a scoring matrix for students and subjects using a dictionary.
Input: students = ['A', 'B'], subjects = ['math', 'sci'], scores = [[90, 80], [85, 95]]
Expected Output: {'A': {'math': 90, 'sci': 80}, 'B': {'math': 85, 'sci': 95}}'''
import ast
students=input("Enter the student list:")
students=ast.literal_eval(students)
subjects=input("Enter the subjects list:")
subjects=ast.literal_eval(subjects)
scores=input("Enter the scores list:")
scores=ast.literal_eval(scores)

scoring_matrix = {student: dict(zip(subjects, student_scores)) for student, student_scores in zip(students, scores)}

print(scoring_matrix)
