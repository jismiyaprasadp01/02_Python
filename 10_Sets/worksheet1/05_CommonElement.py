'''
Python - Check if two lists have at-least one element common    Which set operation shows what you both like?
my_favs = ["Tom", "Jerry", "Ben 10"]
friend_favs = ["Powerpuff", "Jerry", "Scooby"]
Yes! "Jerry" is common.
'''

a = ["Tom", "Jerry", "Ben 10"]
b= ["Powerpuff", "Jerry", "Scooby"]
lis=set(a) & set(b)
print(lis)
