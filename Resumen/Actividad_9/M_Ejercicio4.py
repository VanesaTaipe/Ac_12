from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    with open('large_text_file.txt', 'r') as file:
        lines = file.readlines()
else:
    lines = None

lines = comm.scatter(lines, root=0)

local_word_count = sum(len(line.split()) for line in lines)

total_word_count = comm.reduce(local_word_count, op=MPI.SUM, root=0)

if rank == 0:
    print(f"Total word count: {total_word_count}")
