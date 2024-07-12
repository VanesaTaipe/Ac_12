import threading
import time

lock = threading.Lock()

def low_priority_task():
    while True:
        with lock:
            print("Low priority task")
        time.sleep(0.1)

def high_priority_task():
    while True:
        with lock:
            print("High priority task")
        time.sleep(0.1)

low_thread = threading.Thread(target=low_priority_task)
high_thread = threading.Thread(target=high_priority_task)

low_thread.start()
high_thread.start()

low_thread.join()
high_thread.join()
