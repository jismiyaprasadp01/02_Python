"""
Task: Write a Python function to check if a given list is a palindrome (reads the same forwards and backwards).
Sample input: [1, 2, 3, 2, 1]
Output: True
"""
def is_palindrome(lst):
    return lst == lst[::-1]

nums = [1, 2, 3, 2, 1]
print(is_palindrome(nums))
