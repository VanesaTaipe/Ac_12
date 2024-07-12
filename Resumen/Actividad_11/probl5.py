import threading

class ReadersWriters:
    def __init__(self):
        self.read_count = 0
        self.read_lock = threading.Lock()
        self.resource_lock = threading.Lock()

    def reader(self):
        with self.read_lock:
            self.read_count += 1
            if self.read_count == 1:
                self.resource_lock.acquire()
        print('Reading')
        with self.read_lock:
            self.read_count -= 1
            if self.read_count == 0:
                self.resource_lock.release()

    def writer(self):
        with self.resource_lock:
            print('Writing')

rw = ReadersWriters()
threads = []

for i in range(3):
    t = threading.Thread(target=rw.reader)
    t.start()
    threads.append(t)

for i in range(2):
    t = threading.Thread(target=rw.writer)
    t.start()
    threads.append(t)

for t in threads:
    t.join()
