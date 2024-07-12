## Problema de los filósofos comensales
import threading
import time
import random

N = 5
forks = [threading.Semaphore(1) for _ in range(N)]

def philosopher(id):
    left_fork = id
    right_fork = (id + 1) % N

    while True:
        print(f'Philosopher {id} is thinking.')
        time.sleep(random.random())

        forks[left_fork].acquire()
        print(f'Philosopher {id} picked up left fork {left_fork}.')
        forks[right_fork].acquire()
        print(f'Philosopher {id} picked up right fork {right_fork}.')

        print(f'Philosopher {id} is eating.')
        time.sleep(random.random())

        forks[right_fork].release()
        print(f'Philosopher {id} put down right fork {right_fork}.')
        forks[left_fork].release()
        print(f'Philosopher {id} put down left fork {left_fork}.')

philosophers = [threading.Thread(target=philosopher, args=(i,)) for i in range(N)]
for philosopher_thread in philosophers:
    philosopher_thread.start()
for philosopher_thread in philosophers:
    philosopher_thread.join()
