import threading
import time
import random
from collections import deque

buffer = deque()
buffer_size = 5
semaphore = threading.Semaphore(0)
mutex = threading.Lock()

def producer():
    while True:
        item = random.randint(1, 100)
        time.sleep(random.random())
        mutex.acquire()
        if len(buffer) < buffer_size:
            buffer.append(item)
            print(f"Productor produjo: {item}")
            semaphore.release()
        mutex.release()

def consumer():
    while True:
        semaphore.acquire()
        mutex.acquire()
        item = buffer.popleft()
        print(f"Consumidor consumió: {item}")
        mutex.release()
        time.sleep(random.random())

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()
