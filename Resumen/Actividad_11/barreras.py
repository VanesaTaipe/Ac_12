# threading.Barrier
import threading

def worker(barrier, n):
    print(f'Worker {n} before barrier')
    barrier.wait()
    print(f'Worker {n} after barrier')

if __name__ == "__main__":
    barrier = threading.Barrier(3)
    threads = [threading.Thread(target=worker, args=(barrier, i)) for i in range(3)]

    for t in threads:
        t.start()
    for t in threads:
        t.join()
