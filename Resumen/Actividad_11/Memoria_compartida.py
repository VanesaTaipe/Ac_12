from multiprocessing import Process, Value

def worker(shared_value):
    shared_value.value += 1

if __name__ == "__main__":
    shared_value = Value('i', 0)
    processes = [Process(target=worker, args=(shared_value,)) for _ in range(5)]

    for p in processes:
        p.start()
    for p in processes:
        p.join()

    print(shared_value.value)
