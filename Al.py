import time
from queue import PriorityQueue

# Algoritmo de Berkeley
class BerkeleyNode:
    def __init__(self, node_id, time):
        self.node_id = node_id
        self.time = time

    def adjust_time(self, offset):
        self.time += offset

def berkeley_sync(nodes):
    avg_time = sum(node.time for node in nodes) / len(nodes)
    for node in nodes:
        node.adjust_time(avg_time - node.time)
    return [(node.node_id, node.time) for node in nodes]

# Algoritmo de Lamport
class LamportMutex:
    def __init__(self, node_id, num_nodes):
        self.node_id = node_id
        self.num_nodes = num_nodes
        self.clock = 0
        self.queue = PriorityQueue()
        self.replies = 0

    def request_cs(self):
        self.clock += 1
        self.queue.put((self.clock, self.node_id))
        self.replies = 0
        # Simular envío de mensajes
        print(f"Nodo {self.node_id} solicita sección crítica")

    def release_cs(self):
        self.queue.get()
        # Simular envío de mensajes
        print(f"Nodo {self.node_id} libera sección crítica")

# Algoritmo de Marzullo
def marzullo(times):
    events = []
    for t, error in times:
        events.append((t - error, 1))
        events.append((t + error, -1))
    events.sort()

    count = 0
    max_count = 0
    best_time = None
    for time, change in events:
        count += change
        if count > max_count:
            max_count = count
            best_time = time
    return best_time

# Algoritmo de Mark-Sweep
class MarkSweepCollector:
    def __init__(self, size):
        self.memory = [None] * size
        self.marked = [False] * size

    def allocate(self, obj):
        for i in range(len(self.memory)):
            if self.memory[i] is None:
                self.memory[i] = obj
                return i
        return None  # No hay espacio disponible

    def mark_sweep(self):
        # Marcar
        for obj in self.memory:
            if obj is not None:
                self.marked[self.memory.index(obj)] = True
        
        # Barrer
        for i in range(len(self.memory)):
            if not self.marked[i]:
                self.memory[i] = None
            self.marked[i] = False

# Sistema de reservas
class ReservationSystem:
    def __init__(self, num_nodes, num_rooms):
        self.nodes = [BerkeleyNode(i, time.time()) for i in range(num_nodes)]
        self.mutexes = [LamportMutex(i, num_nodes) for i in range(num_nodes)]
        self.rooms = [False] * num_rooms  # False significa disponible
        self.collector = MarkSweepCollector(100)  # 100 es un tamaño arbitrario

    def synchronize_clocks(self):
        return berkeley_sync(self.nodes)

    def reserve_room(self, node_id, room_id):
        mutex = self.mutexes[node_id]
        mutex.request_cs()
        if not self.rooms[room_id]:
            self.rooms[room_id] = True
            reservation = object()
            self.collector.allocate(reservation)
            print(f"Nodo {node_id} reservó la sala {room_id}")
            result = True
        else:
            print(f"Sala {room_id} no disponible")
            result = False
        mutex.release_cs()
        return result

    def get_precise_time(self):
        times = [(node.time, 1) for node in self.nodes]  # 1 es una incertidumbre arbitraria
        return marzullo(times)

# Ejemplo de uso
if __name__ == "__main__":
    system = ReservationSystem(3, 2)
    
    print("Sincronizando relojes:")
    print(system.synchronize_clocks())

    print("\nReservando salas:")
    system.reserve_room(0, 0)
    system.reserve_room(1, 1)
    system.reserve_room(2, 0)  # Debería fallar

    print("\nTiempo preciso del sistema:")
    print(system.get_precise_time())

    print("\nRecolección de basura:")
    system.collector.mark_sweep()
