import threading

counter = 0

def increment():
    global counter
    for _ in range(100000):
        counter += 1

threads = []
for _ in range(5):
    t = threading.Thread(target=increment)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("Counter without lock:", counter)

# Parte B: Usando Lock
counter = 0
lock = threading.Lock()

def increment_with_lock():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

threads = []
for _ in range(5):
    t = threading.Thread(target=increment_with_lock)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("Counter with lock:", counter)
