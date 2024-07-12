import random
import numpy as np
import time

def prefetch_data(array, indices, prefetch_distance):
    for i in range(len(indices) - prefetch_distance):
        _ = array[indices[i + prefetch_distance]]  # Prefetch
        array[indices[i]] += 1  # Access

size = 10**6
array = np.zeros(size)
indices = list(range(size))
random.shuffle(indices)
prefetch_distance = 10

start_time = time.perf_counter()
prefetch_data(array, indices, prefetch_distance)
end_time = time.perf_counter()

total_time = end_time - start_time
print(f"Tiempo con prefetching: {total_time:.6f} segundos")