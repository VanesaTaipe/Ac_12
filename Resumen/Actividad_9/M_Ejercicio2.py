from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

vector_size = 1000000
local_size = vector_size // size

if rank == 0:
    A = np.random.rand(vector_size)
    B = np.random.rand(vector_size)
else:
    A = None
    B = None

local_A = np.empty(local_size, dtype='d')
local_B = np.empty(local_size, dtype='d')

comm.Scatter(A, local_A, root=0)
comm.Scatter(B, local_B, root=0)

local_C = local_A + local_B

if rank == 0:
    C = np.empty(vector_size, dtype='d')
else:
    C = None

comm.Gather(local_C, C, root=0)

if rank == 0:
    print("Vector addition completed.")

