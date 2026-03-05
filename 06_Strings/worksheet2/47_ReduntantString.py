'''Remove Redundant Substrings from a List
Explanation: From a list of strings, remove repeated substring patterns.
Input: ["hellohello", "world", "testtesttest"]
Expected Output: ["hello", "world", "test"]'''

words = ["hellohello", "world", "testtesttest"]
result = []
for w in words:
    n = len(w)
    for i in range(1, n+1):
        sub = w[:i]
        if sub * (n//i) == w:
            result.append(sub)
            break

print(result)
