'''Remove Redundant Substrings from a List
Explanation: From a list of strings, remove repeated substring patterns.
Input: ["hellohello", "world", "testtesttest"]
Expected Output: ["hello", "world", "test"]'''

import ast


def remove_redundant_substrings(lst):
    res = []

    for word in lst:
        found = False
        for i in range(1, len(word) // 2 + 1):
            part = word[:i]
            if part * (len(word) // len(part)) == word:
                res.append(part)
                found = True
                break
        if not found:
            res.append(word)

    return res


test_list = input("Enter the list")
test_list=ast.literal_eval(test_list) 
output_list = remove_redundant_substrings(test_list)
print("Filtered Output:", output_list)
