from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

# Simulación de acceso
cache = LRUCache(5)
operations = [("put", 1, "data1"), ("put", 2, "data2"), ("get", 1), ("put", 3, "data3"),
              ("put", 4, "data4"), ("put", 5, "data5"), ("get", 2), ("put", 6, "data6"),
              ("get", 3), ("get", 1)]

for op in operations:
    if op[0] == "put":
        cache.put(op[1], op[2])
        print(f"Put: {op[1]} -> {op[2]}")
    elif op[0] == "get":
        result = cache.get(op[1])
        print(f"Get: {op[1]} -> {result}")
    print(f"Estado de la caché: {list(cache.cache.items())}")