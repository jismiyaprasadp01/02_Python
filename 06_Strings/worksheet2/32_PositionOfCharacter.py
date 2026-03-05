#Find the Position of a Character in the k-th Word
text = "hello world python"
k = 2
ch = "o"
words = text.split()
word = words[k-1]
print(word.find(ch))
