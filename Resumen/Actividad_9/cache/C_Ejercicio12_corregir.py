import multiprocessing
import numpy as np
import time
def coherence_worker(shared_array, start, end):
    for i in range(start, end):
        shared_array[i] += 1

size = 10**6
shared_array = multiprocessing.Array('d', size)
num_processes = 4
chunk_size = size // num_processes
processes = []

for i in range(num_processes):
    start = i * chunk_size
    end = (i + 1) * chunk_size
    process = multiprocessing.Process(target=coherence_worker, args=(shared_array, start, end))
    processes.append(process)

start_time = time.perf_counter()

for process in processes:
    process.start()

for process in processes:
    process.join()

end_time = time.perf_counter()
total_time = end_time - start_time

print(f"Tiempo total con coherencia de caché y {num_processes} procesos: {total_time:.6f} segundos")