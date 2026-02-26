"""
Task: Write a Python function to find the longest common subsequence between two lists.
Sample input: [1, 3, 4, 1, 2, 3, 4, 1], [3, 4, 1, 2, 1, 3]
Output: [3, 4, 1, 3]
"""
def lcs(a, b):
    m, n = len(a), len(b)
    dp = [[[] for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m):
        for j in range(n):
            if a[i] == b[j]:
                dp[i+1][j+1] = dp[i][j] + [a[i]]
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j], key=len)

    return dp[m][n]

a = [1, 3, 4, 1, 2, 3, 4, 1]
b = [3, 4, 1, 2, 1, 3]

print(lcs(a, b))
