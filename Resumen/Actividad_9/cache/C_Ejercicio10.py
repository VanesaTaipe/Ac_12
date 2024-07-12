from concurrent.futures import ThreadPoolExecutor
import random
import numpy as np
def prefetching_worker(array, indices, prefetch_distance):
    for i in range(len(indices) - prefetch_distance):
        _ = array[indices[i + prefetch_distance]]  # Prefetch
        array[indices[i]] += 1  # Access

size = 10**6
array = np.zeros(size)
indices = list(range(size))
random.shuffle(indices)
prefetch_distance = 10

with ThreadPoolExecutor(max_workers=4) as executor:
    futures = [executor.submit(prefetching_worker, array, indices[i::4], prefetch_distance) for i in range(4)]
    
    for future in futures:
        future.result()

print(f"Prefetching completado")