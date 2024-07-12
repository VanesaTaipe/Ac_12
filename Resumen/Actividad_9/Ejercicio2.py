from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    data = "Hello from rank 0"
    for i in range(1, size):
        comm.send(data, dest=i)
    
else:
    data = comm.recv(source=0)
    print(f"Rank {rank} received data: {data}")
