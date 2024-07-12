from mpi4py import MPI
from threading import Thread

def process_data(data_segment):
    result = [x ** 2 for x in data_segment]
    print(f"Processed segment: {result}")

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

data = None
if rank == 0:s
    data = list(range(100))
    segment_size = len(data) // size
    data_segments = [data[i * segment_size:(i + 1) * segment_size] for i in range(size)]
else:
    data_segments = None

data_segment = comm.scatter(data_segments, root=0)

threads = []
for i in range(4):
    t = Thread(target=process_data, args=(data_segment[i::4],))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

comm.Barrier()

if rank == 0:
    print("All data processed.")
