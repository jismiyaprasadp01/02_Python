#Remove After a Substring

s = "Hello world python"
sub = "world"
pos = s.find(sub)
result = s[:pos + len(sub)]
print(result)
