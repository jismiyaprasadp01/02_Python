#Split String into Groups of n Characters

def fun(s, n):
    return [s[i:i+n] for i in range(0, len(s), n)]

s = "abcdefgh"
n = 3

output = fun(s,n)
print(output)
