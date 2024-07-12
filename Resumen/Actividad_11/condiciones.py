#threading.Condition
import threading

class SharedResource:
    def __init__(self):
        self.value = 0
        self.condition = threading.Condition()

    def wait_for_increment(self):
        with self.condition:
            self.condition.wait_for(lambda: self.value > 0)
            print('Value incremented:', self.value)

    def increment(self):
        with self.condition:
            self.value += 1
            self.condition.notify_all()

def worker(resource):
    resource.increment()

def waiter(resource):
    resource.wait_for_increment()

if __name__ == "__main__":
    resource = SharedResource()
    t1 = threading.Thread(target=worker, args=(resource,))
    t2 = threading.Thread(target=waiter, args=(resource,))

    t2.start()
    t1.start()
    t1.join()
    t2.join()
