import threading

class SharedResource:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            self.value += 1

resource = SharedResource()

def worker():
    for _ in range(100000):
        resource.increment()

threads = [threading.Thread(target=worker) for _ in range(5)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print(resource.value) 
