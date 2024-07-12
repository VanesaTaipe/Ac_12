import threading

def task_1():
    print("Task 1: Executing")

def task_2():
    print("Task 2: Executing")

def task_3():
    print("Task 3: Executing")

def task_4():
    print("Task 4: Executing")

def main():
    threads = []
    tasks = [task_1, task_2, task_3, task_4]
    for task in tasks:
        thread = threading.Thread(target=task)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
