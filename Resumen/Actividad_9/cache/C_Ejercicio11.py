import numpy as np
import time

def locality_optimized_algorithm(matrix):
    n = len(matrix)
    result = np.zeros((n, n))
    
    for i in range(n):
        for j in range(n):
            result[i][j] = matrix[i][j] + matrix[j][i]
    
    return result

n = 1000
matrix = np.random.rand(n, n)

start_time = time.perf_counter()
result = locality_optimized_algorithm(matrix)
end_time = time.perf_counter()

print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")