import threading
import queue

def worker(task_queue, result_queue):
    while True:
        task = task_queue.get()
        if task is None:
            break
        result = task * task
        result_queue.put(result)
        task_queue.task_done()

task_queue = queue.Queue()
result_queue = queue.Queue()

num_workers = 4
workers = []
for _ in range(num_workers):
    t = threading.Thread(target=worker, args=(task_queue, result_queue))
    t.start()
    workers.append(t)

# Agregar tareas a la cola
for i in range(20):
    task_queue.put(i)

# esperar por todas las tareas a ser procesadas
task_queue.join()

# parar los trabajadores
for _ in range(num_workers):
    task_queue.put(None)

for t in workers:
    t.join()

# imprimir resultados
while not result_queue.empty():
    print(result_queue.get())
