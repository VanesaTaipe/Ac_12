import threading
import time

shared_memory = [0] * 10
bus_operations = []
bus_lock = threading.Lock()

class Cache:
    def __init__(self, id):
        self.id = id
        self.cache = [0] * 10

    def read(self, index):
        with bus_lock:
            bus_operations.append((self.id, 'read', index))
        return self.cache[index]

    def write(self, index, value):
        with bus_lock:
            bus_operations.append((self.id, 'write', index, value))
        self.cache[index] = value

    def snoop(self):
        while True:
            with bus_lock:
                if bus_operations:
                    op = bus_operations.pop(0)
                    if op[1] == 'write':
                        self.cache[op[2]] = op[3]
            time.sleep(0.01)

def cpu_task(cache, index, value):
    cache.write(index, value)
    print(f"CPU {cache.id} wrote {value} at index {index}")
    time.sleep(1)
    read_value = cache.read(index)
    print(f"CPU {cache.id} read {read_value} from index {index}")

def main():
    caches = [Cache(i) for i in range(4)]
    threads = []

    for cache in caches:
        t = threading.Thread(target=cache.snoop)
        t.daemon = True
        t.start()

    for i, cache in enumerate(caches):
        t = threading.Thread(target=cpu_task, args=(cache, i % 10, i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
