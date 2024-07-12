import threading
import queue

ricart_agrawala_queue = queue.Queue()

def request_critical_section(node_id):
    global lamport_clock
    lamport_clock += 1
    ricart_agrawala_queue.put((lamport_clock, node_id))
    print(f"Node {node_id} requested critical section with timestamp: {lamport_clock}")

def receive_request():
    while True:
        if not ricart_agrawala_queue.empty():
            timestamp, node_id = ricart_agrawala_queue.get()
            print(f"Received request from Node {node_id} with timestamp: {timestamp}")

t1 = threading.Thread(target=request_critical_section, args=(1,))
t2 = threading.Thread(target=receive_request)

t1.start()
t2.start()

t1.join()
t2.join()
