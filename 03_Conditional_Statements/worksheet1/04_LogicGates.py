"""
Given two pin logic levels (0 or 1), print the type of logic gate output if these were inputs to an AND, OR, and XOR gate.
Input: 1, 0
Output: AND: 0, OR: 1, XOR: 1
"""
a, b = map(int, input("Enter two logic levels (0 or 1): ").split())

print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)
