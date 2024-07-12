import threading
import time

class Philosopher(threading.Thread):
    def __init__(self, name, left_fork, right_fork):
        threading.Thread.__init__(self, name=name)
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        while True:
            time.sleep(1)
            self.dine()

    def dine(self):
        fork1, fork2 = self.left_fork, self.right_fork
        while True:
            fork1.acquire(True)
            locked = fork2.acquire(False)
            if locked: break
            fork1.release()
            fork1, fork2 = fork2, fork1
        self.eating()
        fork2.release()
        fork1.release()

    def eating(self):
        print(f'{self.name} is eating.')
        time.sleep(1)

forks = [threading.Lock() for n in range(5)]
names = ['Philosopher1', 'Philosopher2', 'Philosopher3', 'Philosopher4', 'Philosopher5']

philosophers = [Philosopher(names[i], forks[i], forks[(i+1)%5]) for i in range(5)]

for p in philosophers:
    p.start()
