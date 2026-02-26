"""
Task: Write a Python function to find the length of the longest increasing sub-sequence in a list of numbers.
Sample input: [10, 22, 9, 33, 21, 50, 41, 60, 80]
Output: 6
(The longest increasing subsequence is [10, 22, 33, 50, 60, 80])
"""
def lis(nums):
    dp = [1] * len(nums)

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

nums = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(lis(nums))
