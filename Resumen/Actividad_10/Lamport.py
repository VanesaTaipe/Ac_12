## Codigo inicial del algoritmo de Lamport
import threading
import time
import random

class LamportClock:
    def __init__(self, pid):
        self.clock = 0
        self.pid = pid

    def increment(self):
        self.clock += 1

    def update(self, timestamp):
        self.clock = max(self.clock, timestamp) + 1

    def get_time(self):
        return self.clock

class Process:
    def __init__(self, pid, total_processes):
        self.pid = pid
        self.clock = LamportClock(pid)
        self.total_processes = total_processes
        self.request_queue = []

    def request_resource(self):
        self.clock.increment()
        timestamp = self.clock.get_time()
        request = (timestamp, self.pid)
        self.request_queue.append(request)
        self.request_queue.sort()
        return request

    def receive_request(self, timestamp, pid):
        self.clock.update(timestamp)
        self.request_queue.append((timestamp, pid))
        self.request_queue.sort()

    def release_resource(self):
        self.request_queue.pop(0)

    def can_enter_critical_section(self):
        if self.request_queue:
            return self.request_queue[0][1] == self.pid
        return False

def simulate_process(process):
    while True:
        time.sleep(random.uniform(0.5, 2))
        request = process.request_resource()
        print(f"Process {process.pid} requested resource at time {request[0]}")

        # Simulate receiving requests from other processes
        for i in range(process.total_processes):
            if i != process.pid:
                process.receive_request(random.randint(0, 10), i)

        while not process.can_enter_critical_section():
            time.sleep(0.1)
        
        print(f"Process {process.pid} entering critical section at time {process.clock.get_time()}")
        time.sleep(random.uniform(0.5, 1.5))
        print(f"Process {process.pid} leaving critical section at time {process.clock.get_time()}")
        process.release_resource()

total_processes = 3
processes = [Process(i, total_processes) for i in range(total_processes)]
threads = [threading.Thread(target=simulate_process, args=(p,)) for p in processes]

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
