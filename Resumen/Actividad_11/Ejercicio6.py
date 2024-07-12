import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()

def task1():
    while True:
        with lock1:
            time.sleep(0.1)
            with lock2:
                print("Task 1 completed")
        time.sleep(0.1)

def task2():
    while True:
        with lock2:
            time.sleep(0.1)
            with lock1:
                print("Task 2 completed")
        time.sleep(0.1)

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()
