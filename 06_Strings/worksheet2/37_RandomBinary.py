#Generate a Random Binary String

import random

def random_binary_string(length):
    return ''.join(random.choice('01') for _ in range(length))

length = 8
output = random_binary_string(length)
print(output)
