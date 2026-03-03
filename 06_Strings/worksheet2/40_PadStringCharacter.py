#Pad a String with Characters

def pad_string(s, total_length, pad_char):
    return s.rjust(total_length, pad_char)

input = "cat"
length = 6
pad_char = "*"

output = pad_string(input, length, pad_char)
print(output)
