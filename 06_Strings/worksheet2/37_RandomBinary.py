#Generate a Random Binary String
import random
s = ""
for i in range(5):
    s = s + str(random.randint(0,1))

print(s)
