from multiprocessing import Process, Queue
import time
import random

def producer(queue):
    for _ in range(5):
        item = random.randint(1, 1000)
        queue.put(item)
        print(f"Produced {item}")
        time.sleep(random.random())

def consumer(queue):
    while True:
        item = queue.get()
        if item is None:  # Sentinel value to indicate end of processing
            break
        print(f"Consumed {item}")
        time.sleep(random.random())

if __name__ == "__main__":
    queue = Queue()

    producers = [Process(target=producer, args=(queue,)) for _ in range(2)]
    consumers = [Process(target=consumer, args=(queue,)) for _ in range(2)]

    for p in producers:
        p.start()

    for c in consumers:
        c.start()

    for p in producers:
        p.join()

    # Add sentinel values to the queue to signal consumers to exit
    for _ in consumers:
        queue.put(None)

    for c in consumers:
        c.join()

