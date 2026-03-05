#Split String into Groups of n Characters

s = "abcdefghi"
n = 3
result = []
for i in range(0, len(s), n):
    result.append(s[i:i+n])
print(result)
