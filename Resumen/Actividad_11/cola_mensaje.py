import multiprocessing

def worker(queue):
    queue.put("Hello from worker")

if __name__ == "__main__":
    queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=worker, args=(queue,))
    process.start()
    print(queue.get())
    process.join()
