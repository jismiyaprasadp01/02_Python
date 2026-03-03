'''LRU Cache Using OrderedDict
Implement a Least Recently Used (LRU) cache and show its contents after several operations.
Input: operations = ['put 1', 'put 2', 'get 1', 'put 3'], capacity = 2
Expected Output: [1, 3]'''

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key) 
            return self.cache[key]
        return -1

    def put(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = True  
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  

    def get_keys(self):
        return list(self.cache.keys())

operations = ['put 1', 'put 2', 'get 1', 'put 3']
capacity = 2

lru = LRUCache(capacity)

for op in operations:
    parts = op.split()
    if parts[0] == 'put':
        lru.put(int(parts[1]))
    elif parts[0] == 'get':
        lru.get(int(parts[1]))

print(lru.get_keys())
