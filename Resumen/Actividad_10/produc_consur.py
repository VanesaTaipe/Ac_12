## Algoritmo de productores y consumidores
import threading
import time
import random

buffer = []
buffer_size = 10

empty = threading.Semaphore(buffer_size)
full = threading.Semaphore(0)
mutex = threading.Semaphore(1)

def producer():
    while True:
        item = random.randint(1, 100)
        empty.acquire()
        mutex.acquire()
        buffer.append(item)
        print(f'Producer produced {item}')
        mutex.release()
        full.release()
        time.sleep(random.random())

def consumer():
    while True:
        full.acquire()
        mutex.acquire()
        item = buffer.pop(0)
        print(f'Consumer consumed {item}')
        mutex.release()
        empty.release()
        time.sleep(random.random())

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)
producer_thread.start()
consumer_thread.start()
producer_thread.join()
consumer_thread.join()
