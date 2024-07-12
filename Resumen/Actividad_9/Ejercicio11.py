from mpi4py import MPI
from threading import Thread

def compute_square(value, result_list, index):
    result_list[index] = value ** 2

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

data = None
if rank == 0:
    data = list(range(1, 101))
    segment_size = len(data) // size
    data_segments = [data[i * segment_size:(i + 1) * segment_size] for i in range(size)]
else:
    data_segments = None

data_segment = comm.scatter(data_segments, root=0)

results = [0] * len(data_segment)
threads = []
for i in range(len(data_segment)):
    t = Thread(target=compute_square, args=(data_segment[i], results, i))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

gathered_results = comm.gather(results, root=0)

if rank == 0:
    final_results = [item for sublist in gathered_results for item in sublist]
    print(f"Final results: {final_results}")
    print(len(final_results))
