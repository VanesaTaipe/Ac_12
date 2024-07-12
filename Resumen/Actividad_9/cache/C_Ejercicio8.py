from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.freq = defaultdict(OrderedDict)
        self.min_freq = 0

    def get(self, key):
        if key not in self.cache:
            return -1
        freq = self.cache[key][1]
        self.cache[key][1] += 1
        value = self.cache[key][0]
        del self.freq[freq][key]
        if not self.freq[freq]:
            del self.freq[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        self.freq[freq + 1][key] = None
        return value

    def put(self, key, value):
        if self.capacity == 0:
            return
        if key in self.cache:
            self.cache[key][0] = value
            self.get(key)
            return
        if len(self.cache) >= self.capacity:
            evict = next(iter(self.freq[self.min_freq]))
            del self.freq[self.min_freq][evict]
            del self.cache[evict]
        self.cache[key] = [value, 1]
        self.freq[1][key] = None
        self.min_freq = 1

# Simulación de acceso
cache = LFUCache(3)
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