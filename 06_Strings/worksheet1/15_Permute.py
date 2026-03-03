"""
Generate All Permutations of a String
Explanation: List all possible ways to rearrange the characters.
Input: "abc"
Expected Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
"""
def permute(s, ans=""):
    if len(s) == 0:
        print(ans)
        return

    for i in range(len(s)):
        ch = s[i]
        remaining = s[:i] + s[i+1:]
        permute(remaining, ans + ch)

permute("abc")
