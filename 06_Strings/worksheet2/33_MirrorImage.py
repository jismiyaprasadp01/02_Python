#Find the Position of a Character in the k-th Word

def fun(word_list, k, char):
    if k <= 0 or k > len(word_list):
        return "Invalid word index"
    word = word_list[k - 1]
    pos = word.find(char)
    if pos != -1:
        print("Position:", pos)
    else:
        print("Character not found")

words = ["hello", "world"]
k = 2
character = "r"
fun(words, k, character)
