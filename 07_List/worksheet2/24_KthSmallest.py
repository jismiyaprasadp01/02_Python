"""
Task: Write a Python function to find the k-th smallest element in a list.
Sample input: [7, 10, 4, 3, 20, 15], k = 3
Output: 7
"""
def kth_smallest(lst, k):
    lst_sorted = sorted(lst)
    return lst_sorted[k-1]

nums = [7, 10, 4, 3, 20, 15]
print(kth_smallest(nums, 3))
