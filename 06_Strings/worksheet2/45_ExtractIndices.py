#Extract Indices of Substring Matches

def find_substring_indices(text, substring):
    indices = []
    for i in range(len(text) - len(substring) + 1):
        if text[i:i+len(substring)] == substring:
            indices.append(i)
    return indices

text = "abracadabra"
substring = "abra"

output = find_substring_indices(text, substring)
print(output)
