import threading

barrier = threading.Barrier(3)

def stage(worker_id):
    print(f"Hilo {worker_id} esperando en la barrera.")
    barrier.wait()
    print(f"Hilo {worker_id} pasó la barrera.")

threads = [threading.Thread(target=stage, args=(i,)) for i in range(3)]
for t in threads:
    t.start()
for t in threads:
    t.join()
