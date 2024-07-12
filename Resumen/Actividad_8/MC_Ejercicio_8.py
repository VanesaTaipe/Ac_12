import threading

shared_value = 0
lock = threading.Lock()

def modify_shared_value():
    global shared_value
    for _ in range(10000):
        with lock:
            temp = shared_value
            temp += 1
            shared_value = temp

def main():
    threads = []

    for _ in range(4):
        t = threading.Thread(target=modify_shared_value)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"Final value: {shared_value}")

if __name__ == "__main__":
    main()
