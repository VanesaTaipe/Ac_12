# Deadlock
lock1 = threading.Lock()
lock2 = threading.Lock()

def deadlock_thread_1():
    with lock1:
        time.sleep(0.1)
        with lock2:
            print("Hilo 1 completado")

def deadlock_thread_2():
    with lock2:
        time.sleep(0.1)
        with lock1:
            print("Hilo 2 completado")

# Livelock
def livelock_thread_1():
    while True:
        with lock1:
            if not lock2.locked():
                print("Livelock evitado por Hilo 1")
                break
            print("Hilo 1 reintentando...")
            time.sleep(0.1)

def livelock_thread_2():
    while True:
        with lock2:
            if not lock1.locked():
                print("Livelock evitado por Hilo 2")
                break
            print("Hilo 2 reintentando...")
            time.sleep(0.1)

# Ejecución
thread1 = threading.Thread(target=deadlock_thread_1)
thread2 = threading.Thread(target=deadlock_thread_2)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
