import multiprocessing

def increment(shared_value, lock):
    for _ in range(10000):
        with lock:
            shared_value.value += 1

def main():
    shared_value = multiprocessing.Value('i', 0)
    lock = multiprocessing.Lock()
    processes = []

    for _ in range(4):
        p = multiprocessing.Process(target=increment, args=(shared_value, lock))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f"Final value: {shared_value.value}")

if __name__ == "__main__":
    main()
