#Filter Strings with a Combination of k Substrings

def filter_by_substrings(strings, substrings):
    return [s for s in strings if all(sub in s for sub in substrings)]

input_list = ["applebanana", "apple", "banana", "applebananacherry"]
required_substrings = ["apple", "banana"]

output = filter_by_substrings(input_list, required_substrings)
print(output)
