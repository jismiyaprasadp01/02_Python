''' The Magic Dictionary of Hogwarts
Every student at Hogwarts has a pet. Sometimes, a student forgets to register a pet. 
If someone asks for Hermione’s pet, and her name isn’t registered, you must politely tell them 
“No record, maybe try another student!” Can you build this polite pet query?
Input: pets = {'Harry': 'owl', 'Ron': 'rat'}, query = 'Hermione'
Expected Output: No record, maybe try another student!'''

import ast
pets=input("Enter the pets details:")
pets=ast.literal_eval(pets)

query=input("Enter the item to check its pets availability:")

if query in pets:
    print(f"{query}'s pet is a {pets[query]}")
else:
    print("No record, maybe try another student!")
