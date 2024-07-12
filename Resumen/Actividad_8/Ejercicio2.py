import numpy as np
from joblib import Parallel, delayed

def multiply_sub_matrices(A, B):
    return np.dot(A, B)

def parallel_matrix_multiplication():
    A = np.random.rand(1000, 1000)
    B = np.random.rand(1000, 1000)
    A_subs = np.array_split(A, 4, axis=0)
    B_subs = np.array_split(B, 4, axis=1)

    results = Parallel(n_jobs=4)(delayed(multiply_sub_matrices)(A_sub, B_sub) for A_sub in A_subs for B_sub in B_subs)
    
    C = np.zeros((1000, 1000))
    for i, res in enumerate(results):
              C[i*250:(i+1)*250, :] = res
    return C

C = parallel_matrix_multiplication()
print(C)
print(C.shape)
