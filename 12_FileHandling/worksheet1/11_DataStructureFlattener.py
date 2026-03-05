''' Nested Data Structure Flattener
 • Concepts: Handling nested dictionaries/lists, recursion or iterative approaches, and data 
transformation using comprehensions.
 • Description:
 Create a script that accepts a nested dictionary (for example, loaded from a JSON file) and 
flattens it into a single-level dictionary. Use a separator (like an underscore) to concatenate 
nested keys into new single keys.
 • Validation:
 Use a sample nested structure to verify that the output dictionary correctly maps all nested 
values to single-level keys.'''

data = {
    "user": {"name": "John", "age": 25},
    "city": "London"
}

flat = {}

for key in data:
    if type(data[key]) == dict:
        for k in data[key]:
            flat[key + "_" + k] = data[key][k]
    else:
        flat[key] = data[key]

print(flat)
