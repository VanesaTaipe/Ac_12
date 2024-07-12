import threading
import queue
import time

buffer = queue.Queue(maxsize=10)

def producer():
    for i in range(20):
        buffer.put(i)
        print(f'Produced {i}')
        time.sleep(0.1)

def consumer():
    for i in range(20):
        item = buffer.get()
        print(f'Consumed {item}')
        buffer.task_done()
        time.sleep(0.2)

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()
