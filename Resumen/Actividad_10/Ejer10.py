import threading
import time
import random

N = 5
chopsticks = [threading.Lock() for _ in range(N)]

def philosopher(id):
    left = id
    right = (id + 1) % N
    while True:
        time.sleep(random.uniform(0.1, 1))
        print(f"Philosopher {id} is thinking.")
        with chopsticks[left]:
            with chopsticks[right]:
                print(f"Philosopher {id} is eating.")
                time.sleep(random.uniform(0.1, 1))

threads = [threading.Thread(target=philosopher, args=(i,)) for i in range(N)]
for t in threads:
    t.start()

for t in threads:
    t.join()
