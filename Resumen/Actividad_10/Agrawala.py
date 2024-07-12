## Codigo inicial del algoritmo de Ricart-Agrawala
import threading
import time
import random

class RicartAgrawala:
    def __init__(self, pid, total_processes):
        self.pid = pid
        self.clock = 0
        self.total_processes = total_processes
        self.request_queue = []
        self.deferred_replies = []
        self.requesting_cs = False
        self.lock = threading.Lock()

    def request_resource(self):
        with self.lock:
            self.clock += 1
            self.requesting_cs = True
            request = (self.clock, self.pid)
            self.request_queue.append(request)
            self.request_queue.sort()
            return request

    def receive_request(self, timestamp, pid):
        with self.lock:
            self.clock = max(self.clock, timestamp) + 1
            request = (timestamp, pid)
            self.request_queue.append(request)
            self.request_queue.sort()
            if self.requesting_cs and (timestamp, pid) < (self.clock, self.pid):
                self.deferred_replies.append(pid)
            else:
                return True
        return False

    def receive_reply(self, pid):
        with self.lock:
            self.deferred_replies.remove(pid)

    def release_resource(self):
        with self.lock:
            self.request_queue.pop(0)
            self.requesting_cs = False
            replies = self.deferred_replies[:]
            self.deferred_replies.clear()
        return replies

    def can_enter_critical_section(self):
        with self.lock:
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
        
        print(f"Process {process.pid} entering critical section at time {process.clock}")
        time.sleep(random.uniform(0.5, 1.5))
        print(f"Process {process.pid} leaving critical section at time {process.clock}")
        deferred_replies = process.release_resource()

        # Simulate sending replies to deferred processes
        for pid in deferred_replies:
            print(f"Process {process.pid} sending reply to process {pid}")

total_processes = 3
processes = [RicartAgrawala(i, total_processes) for i in range(total_processes)]
threads = [threading.Thread(target=simulate_process, args=(p,)) for p in processes]

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
