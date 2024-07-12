import threading
import time
import numpy as np
def worker(shared_data, start, end):
    for i in range(start, end):
        shared_data[i] += 1

size = 10**6
shared_data = np.zeros(size)
num_threads = 4
threads = []

chunk_size = size // num_threads
for i in range(num_threads):
    start = i * chunk_size
    end = (i + 1) * chunk_size
    thread = threading.Thread(target=worker, args=(shared_data, start, end))
    threads.append(thread)

start_time = time.perf_counter()

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end_time = time.perf_counter()
total_time = end_time - start_time

print(f"Tiempo total con {num_threads} hilos: {total_time:.6f} segundos")