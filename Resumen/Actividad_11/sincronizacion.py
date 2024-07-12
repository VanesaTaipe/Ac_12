# multiprocessing.Semaphore
from multiprocessing import Process, Semaphore

def worker(sem, n):
    sem.acquire()
    print(f'Worker {n} is in critical section')
    sem.release()

if __name__ == "__main__":
    sem = Semaphore(1)
    processes = [Process(target=worker, args=(sem, i)) for i in range(5)]

    for p in processes:
        p.start()
    for p in processes:
        p.join()
