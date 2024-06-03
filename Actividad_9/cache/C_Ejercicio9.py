import random

class RandomCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

    def get(self, key):
        return self.cache.get(key, -1)

    def put(self, key, value):
        if key not in self.cache:
            if len(self.cache) >= self.capacity:
                evict = random.choice(list(self.cache.keys()))
                del self.cache[evict]
        self.cache[key] = value

# Simulación de acceso
cache = RandomCache(3)
operations = [("put", 1, "data1"), ("put", 2, "data2"), ("put", 3, "data3"), ("get", 1),
              ("put", 4, "data4"), ("get", 2), ("put", 5, "data5"), ("get", 3), ("get", 1)]

for op in operations:
    if op[0] == "put":
        cache.put(op[1], op[2])
        print(f"Put: {op[1]} -> {op[2]}")
    elif op[0] == "get":
        result = cache.get(op[1])
        print(f"Get: {op[1]} -> {result}")
    print(f"Estado de la caché: {list(cache.cache.items())}")