#threading.Lock
import threading

class SharedResource:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            self.value += 1

def worker(resource):
    for _ in range(1000):
        resource.increment()

if __name__ == "__main__":
    resource = SharedResource()
    threads = [threading.Thread(target=worker, args=(resource,)) for _ in range(5)]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print(resource.value)
