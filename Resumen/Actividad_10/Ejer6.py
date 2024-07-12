import threading
import random
import time
from collections import deque

buffer = deque()
buffer_size = 10
empty = threading.Semaphore(buffer_size)
full = threading.Semaphore(0)
mutex = threading.Lock()

def producer():
    while True:
        item = random.randint(1, 100)
        empty.acquire()
        mutex.acquire()
        buffer.append(item)
        print(f"Producer produced: {item}")
        mutex.release()
        full.release()
        time.sleep(random.uniform(0.1, 1))

def consumer():
    while True:
        full.acquire()
        mutex.acquire()
        item = buffer.popleft()
        print(f"Consumer consumed: {item}")
        mutex.release()
        empty.release()
        time.sleep(random.uniform(0.1, 1))

producers = [threading.Thread(target=producer) for _ in range(3)]
consumers = [threading.Thread(target=consumer) for _ in range(3)]

for p in producers:
    p.start()
for c in consumers:
    c.start()
