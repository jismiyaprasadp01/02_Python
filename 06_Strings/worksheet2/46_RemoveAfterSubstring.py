#Remove After a Substring

def remove_after_substring(text, substring):
    index = text.find(substring)
    if index != -1:
        return text[:index + len(substring)]
    return text  # if substring not found, return original text

text = "abcdeFGhiJK"
substring = "FG"

output = remove_after_substring(text, substring)
print(output)
