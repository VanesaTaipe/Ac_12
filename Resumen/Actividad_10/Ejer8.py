import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()

def livelock_thread_1():
    while True:
        with lock1:
            if not lock2.locked():
                with lock2:
                    print("Thread 1 acquired both locks")
                    return
        print("Thread 1 retrying")
        time.sleep(0.1)

def livelock_thread_2():
    while True:
        with lock2:
            if not lock1.locked():
                with lock1:
                    print("Thread 2 acquired both locks")
                    return
        print("Thread 2 retrying")
        time.sleep(0.1)

t1 = threading.Thread(target=livelock_thread_1)
t2 = threading.Thread(target=livelock_thread_2)

t1.start()
t2.start()

t1.join()
t2.join()
