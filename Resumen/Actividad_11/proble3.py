import threading
import queue

buffer = queue.Queue(maxsize=10)

def producer():
    for i in range(100):
        buffer.put(i)
        print(f'Produced {i}')

def consumer():
    for i in range(100):
        item = buffer.get()
        print(f'Consumed {item}')
        buffer.task_done()

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()
