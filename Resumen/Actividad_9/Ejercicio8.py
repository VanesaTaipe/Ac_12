from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = {'key1': 'value1', 'key2': 'value2'}
else:
    data = None

data = comm.bcast(data, root=0)

print(f"Rank {rank} received data: {data}")
