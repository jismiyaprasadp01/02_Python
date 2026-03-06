"""
Task: Write a Python function to find the longest common subsequence between two lists.
Sample input: [1, 3, 4, 1, 2, 3, 4, 1], [3, 4, 1, 2, 1, 3]
Output: [3, 4, 1, 3]
"""

def lcs_simple(a, b):
    result = []
    j = 0

    for i in range(len(a)):
        for k in range(j, len(b)):
            if a[i] == b[k]:
                result.append(a[i])
                j = k + 1
                break

    return result


a = [1, 3, 4, 1, 2, 3, 4, 1]
b = [3, 4, 1, 2, 1, 3]

print(lcs_simple(a, b))
