#Extract Indices of Substring Matches

s = "banana"
sub = "an"

positions = []

for i in range(len(s)):
    if s[i:i+len(sub)] == sub:
        positions.append(i)

print(positions)
