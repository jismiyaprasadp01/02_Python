#Filter Strings with a Combination of k Substrings

words = ["applepie", "applejuice", "bananaapple", "pieapple"]
subs = ["apple", "pie"]
result = []
for w in words:
    if subs[0] in w and subs[1] in w:
        result.append(w)

print(result)
