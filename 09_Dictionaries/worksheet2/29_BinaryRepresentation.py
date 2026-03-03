'''Check if Binary Representations of Two Numbers are Anagrams
Given two numbers, check if their binary representations are anagrams (same bits, just shuffled).
Input: num1 = 5, num2 = 6
Expected Output: False'''

def countSetBits(n) :    
    count = 0
    while n :
        n=n&(n-1)
        count+=1
    return count

def areAnagrams(A, B) :
    return countSetBits(A) == countSetBits(B)


num1 = int(input("Enter the number 1:"))  
num2 = int(input("Enter the number 2:"))    

print(areAnagrams(num1, num2))  
