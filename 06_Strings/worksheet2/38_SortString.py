#Reverse Sort a String

def reverse_sort_string(s):
    return ''.join(sorted(s, reverse=True))

s = "python"
output = reverse_sort_string(s)
print(output)
