from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

num_samples = 1000000
local_samples = num_samples // size

np.random.seed(rank)
local_count = 0

for _ in range(local_samples):
    x, y = np.random.rand(2)
    if x**2 + y**2 <= 1.0:
        local_count += 1

total_count = comm.reduce(local_count, op=MPI.SUM, root=0)

if rank == 0:
    pi_estimate = (4.0 * total_count) / num_samples
    print(f"Estimated Pi: {pi_estimate}")
