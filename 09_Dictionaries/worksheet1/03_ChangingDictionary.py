''' Change Dictionaries
Updating dictionary values is needed when data changes during runtime.
Update the age of 'Anil' from 21 to 22 in this dictionary: ages = {'Anil': 21, 'Sunita': 20}.
Change multiple values at once in the dictionary: info = {'a': 10, 'b': 20} so that both 'a' and 'b' become 100.
Increase every salary in salaries = {'A': 20000, 'B': 30000} by 10%.
Sample Output: {'A': 22000.0, 'B': 33000.0}
Assign a value to a key that doesn't exist (e.g., add 'C': 25000 to salaries). What happens?'''


ages = {'Anil': 21, 'Sunita': 20}
ages['Anil'] = 22
print(ages)

info = {'a': 10, 'b': 20}
info['a'] = 100
info['b'] = 100
print(info)

salaries = {'A': 20000, 'B': 30000}
for i in salaries:
    salaries[i] = salaries[i] * 1.1
print(salaries)

salaries['C'] = 25000
print(salaries)
