from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Cada proceso tiene un número diferente
number = rank + 1

total_sum = comm.reduce(number, op=MPI.SUM, root=0)

if rank == 0:
    print(f"Total sum: {total_sum}")
