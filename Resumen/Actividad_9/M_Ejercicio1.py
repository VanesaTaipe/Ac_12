from multiprocessing import Pool
import numpy as np

def matrix_multiply_segment(args):
    A_segment, B = args
    return np.dot(A_segment, B)

if __name__ == "__main__":
    A = np.random.rand(1000, 1000)
    B = np.random.rand(1000, 1000)

    num_processes = 4
    segment_size = A.shape[0] // num_processes
    segments = [(A[i * segment_size:(i + 1) * segment_size], B) for i in range(num_processes)]

    with Pool(num_processes) as pool:
        results = pool.map(matrix_multiply_segment, segments)

    C = np.vstack(results)
    print("Matrix multiplication completed.")
