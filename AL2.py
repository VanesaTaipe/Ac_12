import threading
import time
from queue import PriorityQueue
#Nodo maestro que coordina la sincronizacion del reloj entre nodos del sistema
class BerkeleyNode:
    def __init__(self, node_id, time):
        self.node_id = node_id
        self.time = time

    def adjust_time(self, offset):
        self.time += offset

class BerkeleyMaster:
    def __init__(self, nodes):
        self.nodes = nodes

    def synchronize_clocks(self):
        times = [node.time for node in self.nodes]
        average_time = sum(times) / len(times)
        for node in self.nodes:
            offset = average_time - node.time
            node.adjust_time(offset)
        return [(node.node_id, node.time) for node in self.nodes]
#Lamport utiliza relojes logicos para mantener un orden total de los eventos y asegurar que los nodos accedan al recurso.
class LamportMutex:
    def __init__(self, node_id, num_nodes):
        self.node_id = node_id
        self.num_nodes = num_nodes
        self.clock = 0
        self.request_queue = PriorityQueue()
        self.replies_received = 0
        self.lock = threading.Lock()

    def send_request(self):
        self.clock += 1
        self.request_queue.put((self.clock, self.node_id))
        for i in range(self.num_nodes):
            if i != self.node_id:
                self.send_message(i, 'REQUEST', self.clock, self.node_id)

    def send_message(self, target, msg_type, timestamp, sender_id):
        # Simular el envío de un mensaje por la red
        print(f"Nodo {self.node_id} enviando {msg_type} al Nodo {target} con timestamp {timestamp}")
        time.sleep(0.1)
        # En una implementación real, este método enviaría el mensaje a través de la red

    def receive_message(self, msg_type, timestamp, sender_id):
        with self.lock:
            self.clock = max(self.clock, timestamp) + 1
            if msg_type == 'REQUEST':
                self.request_queue.put((timestamp, sender_id))
                self.send_message(sender_id, 'REPLY', self.clock, self.node_id)
            elif msg_type == 'REPLY':
                self.replies_received += 1

    def enter_critical_section(self):
        self.send_request()
        while self.replies_received < self.num_nodes - 1:
            time.sleep(0.1)
        print(f"Nodo {self.node_id} ingresando a la sección crítica")

    def leave_critical_section(self):
        with self.lock:
            self.request_queue.get()
        for i in range(self.num_nodes):
            if i != self.node_id:
                self.send_message(i, 'RELEASE', self.clock, self.node_id)
        print(f"Nodo {self.node_id} dejando la sección crítica")
#Permite manejar multiples fuentes de tiempo con diferentes preciones
class MarzulloNode:
    def __init__(self, node_id, time, uncertainty):
        self.node_id = node_id
        self.time = time
        self.uncertainty = uncertainty

    def get_time_interval(self):
        return (self.time - self.uncertainty, self.time + self.uncertainty)

def marzullo_algorithm(nodes):
    intervals = [node.get_time_interval() for node in nodes]
    events = []
    for start, end in intervals:
        events.append((start, +1))
        events.append((end, -1))
    events.sort()

    max_count = 0
    count = 0
    best_interval = None
    for event in events:
        count += event[1]
        if count > max_count:
            max_count = count
            best_interval = event[0]
    
    return best_interval
#LImpiar,recoleta todo lo bueno y barrera la memoria para liberar no marcados
class MarkSweepCollector:
    def __init__(self, size):
        self.size = size
        self.memory = [None] * size
        self.marked = [False] * size
        self.object_to_address = {}

    def allocate(self, obj):
        for i in range(self.size):
            if self.memory[i] is None:
                self.memory[i] = obj
                self.object_to_address[obj] = i
                return i
        self.collect()
        return self.allocate(obj)

    def mark(self, roots):
        for root in roots:
            self._mark(root)

    def _mark(self, obj):
        if obj is not None and obj in self.object_to_address:
            addr = self.object_to_address[obj]
            if not self.marked[addr]:
                self.marked[addr] = True

    def sweep(self):
        for i in range(self.size):
            if not self.marked[i]:
                obj = self.memory[i]
                if obj is not None:
                    del self.object_to_address[obj]
                self.memory[i] = None
            else:
                self.marked[i] = False

    def collect(self):
        self.mark(self.memory)
        self.sweep()
#BerkeleyModel
nodes = [BerkeleyNode(i, time) for i, time in enumerate([10,20,30])]
master = BerkeleyMaster(nodes)
synchronized_times = master.synchronize_clocks()
print(synchronized_times)
# Creación de objetos para exclusión mutua con Lamport
num_nodes = len(nodes)
mutexes = [LamportMutex(i, num_nodes) for i in range(num_nodes)]

# Uso de la exclusión mutua para reservar una sala
mutexes[0].enter_critical_section()
# Realizar operaciones de reserva de sala 
time.sleep(1)
mutexes[0].leave_critical_section()
best_time = marzullo_algorithm([MarzulloNode(i, time, uncertainty) for i, (time, uncertainty) in enumerate([(10, 1), (20, 2), (30, 3)])])

print(best_time)

