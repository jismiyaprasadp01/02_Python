#Replace Multiple Words at Once

def replace_multiple(text, replacements):
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

s = "I like apples and bananas."
replacements = {"apples": "oranges", "bananas": "grapes"}
output = replace_multiple(s, replacements)
print(output)
