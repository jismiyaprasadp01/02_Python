"""
Dictionaries
Dictionaries let you store and organize data using key-value pairs. They are fundamental for mapping, counting, and fast lookups.
Log Session a dictionary to store the roll numbers (as keys) and names (as values) for 3 students.
Sample Output: {101: 'Ravi', 102: 'Priya', 103: 'Amit'}
Suppose you write a dictionary with the same key twice. What value is stored?
Sample Input: d = {'x': 1, 'y': 2, 'x': 5}
Sample Output: {'x': 5, 'y': 2}
How can you check if the key 'fruit' exists in a dictionary called d?
Sample Input: d = {'fruit': 'apple', 'veg': 'carrot'}
Sample Output: True (when checked for 'fruit')
Count the frequency of each letter in the string "apple", store results in a dictionary, and print it.
Sample Input: "apple"
Sample Output: {'a': 1, 'p': 2, 'l': 1, 'e': 1}
"""
students = {
    101: 'Ravi',
    102: 'Priya',
    103: 'Amit'
}

print(students)



d = {'x': 1, 'y': 2, 'x': 5}
print(d)



d = {'fruit': 'apple', 'veg': 'carrot'}
print('fruit' in d)


word = "apple"
freq = {}

for letter in word:
    if letter in freq:
        freq[letter] += 1
    else:
        freq[letter] = 1

print(freq)





