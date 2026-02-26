"""
Task: Write a Python function to find the maximum sum sub-sequence in a list (sub-sequence, not necessarily contiguous).
Sample input: [2, -1, 2, 3, 4, -5]
Output: 11
(The maximum sum subsequence is 2 + 2 + 3 + 4)
"""
def max_sum_subsequence(lst):
    total = 0
    for x in lst:
        if x > 0:
            total += x
    return total

nums = [2, -1, 2, 3, 4, -5]
print(max_sum_subsequence(nums))
