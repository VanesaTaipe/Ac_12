import threading

# Recursos
lock1 = threading.Lock()
lock2 = threading.Lock()

def thread1():
    with lock1:
        print("Hilo 1: ha adquirido lock1")
        with lock2:
            print("Hilo 1: ha adquirido lock2")

def thread2():
    with lock2:
        print("Hilo 2: ha adquirido lock2")
        with lock1:
            print("Hilo 2: ha adquirido lock1")

t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)

t1.start()
t2.start()

t1.join()
t2.join()
