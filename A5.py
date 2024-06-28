import time
import random
from typing import List, Tuple

# Algoritmo de Cristian para sincronización de tiempo
class CristianServer:
    def __init__(self):
        self.time = time.time()

    def get_time(self):
        return self.time

class CristianClient:
    def __init__(self, server):
        self.server = server
        self.time = time.time()

    def synchronize_clock(self):
        request_time = time.time()
        server_time = self.server.get_time()
        response_time = time.time()
        round_trip_time = response_time - request_time
        self.time = server_time + round_trip_time / 2

# Algoritmo de Raymond para exclusión mutua
class RaymondMutex:
    def __init__(self, node_id, parent=None):
        self.node_id = node_id
        self.parent = parent
        self.token_holder = (parent is None)
        self.request_queue = []

    def request_access(self):
        if self.token_holder:
            self.enter_critical_section()
        else:
            self.request_queue.append(self.node_id)
            self.send_request_to_parent()

    def send_request_to_parent(self):
        if self.parent:
            self.parent.receive_request(self)

    def receive_request(self, requester):
        if not self.token_holder:
            self.request_queue.append(requester.node_id)
            self.send_request_to_parent()
        elif requester.node_id == self.node_id:
            self.enter_critical_section()
        else:
            self.send_token(requester)

    def send_token(self, requester):
        self.token_holder = False
        requester.receive_token(self)

    def receive_token(self, sender):
        self.token_holder = True
        if self.request_queue and self.request_queue[0] == self.node_id:
            self.enter_critical_section()
        else:
            self.send_token_to_next_in_queue()

    def send_token_to_next_in_queue(self):
        if self.request_queue:
            next_node_id = self.request_queue.pop(0)
            next_node = [node for node in nodes if node.node_id == next_node_id][0]
            self.send_token(next_node)

    def enter_critical_section(self):
        print(f"Nodo {self.node_id} ingresando a la sección crítica")
        # Código de sección crítica aquí
        self.leave_critical_section()

    def leave_critical_section(self):
        print(f"Nodo {self.node_id} dejando la sección crítica")
        if self.request_queue:
            self.send_token_to_next_in_queue()

# Algoritmo de marcado-compacto para recolección de basura
class MarkCompactCollector:
    def __init__(self, size):
        self.size = size
        self.memory = [None] * size
        self.marked = [False] * size

    def allocate(self, obj):
        for i in range(self.size):
            if self.memory[i] is None:
                self.memory[i] = obj
                return i
        self.collect()
        return self.allocate(obj)

    def mark(self, roots):
        for root in roots:
            self._mark(root)

    def _mark(self, obj):
        if obj is not None:
            addr = self.memory.index(obj)
            if not self.marked[addr]:
                self.marked[addr] = True

    def compact(self):
        new_memory = [None] * self.size
        j = 0
        for i in range(self.size):
            if self.marked[i]:
                new_memory[j] = self.memory[i]
                j += 1
        self.memory = new_memory

    def collect(self):
        self.mark(self.memory)
        self.compact()
        self.marked = [False] * self.size

# Protocolo de Tolerancia a Fallos Bizantina simplificado
class ByzantineNode:
    def __init__(self, node_id, is_malicious=False):
        self.node_id = node_id
        self.is_malicious = is_malicious

    def get_monitoring_data(self) -> float:
        if self.is_malicious:
            return random.uniform(0, 100)  # Dato falso
        else:
            return 50.0  # Dato real simulado

def byzantine_consensus(nodes: List[ByzantineNode]) -> float:
    data = [node.get_monitoring_data() for node in nodes]
    data.sort()
    n = len(data)
    f = (n - 1) // 3  # Máximo número de nodos maliciosos tolerados
    return sum(data[f:-f]) / (n - 2*f)  # Promedio de los valores del medio

# Sistema de Monitoreo de Red
class NetworkMonitoringSystem:
    def __init__(self, num_nodes):
        self.time_server = CristianServer()
        self.nodes = [ByzantineNode(i, is_malicious=(random.random() < 0.2)) for i in range(num_nodes)]
        self.mutexes = [RaymondMutex(i) for i in range(num_nodes)]
        self.collector = MarkCompactCollector(num_nodes * 2)  # Espacio para datos y metadatos
        
        # Configurar la estructura de árbol para Raymond
        for i in range(1, num_nodes):
            self.mutexes[i].parent = self.mutexes[(i-1)//2]

    def synchronize_clocks(self):
        for node in self.nodes:
            client = CristianClient(self.time_server)
            client.synchronize_clock()
            print(f"Nodo {node.node_id} sincronizado. Tiempo: {client.time}")

    def monitor_network(self):
        consensus_data = byzantine_consensus(self.nodes)
        print(f"Datos de monitoreo consensuados: {consensus_data}")

        # Simular acceso a datos de monitoreo
        for mutex in self.mutexes:
            mutex.request_access()
            time.sleep(0.1)  # Simular trabajo en sección crítica

        # Simular almacenamiento de datos
        for _ in range(len(self.nodes)):
            addr = self.collector.allocate(f"Data_{_}")
            print(f"Dato almacenado en dirección: {addr}")

        # Forzar recolección de basura
        self.collector.collect()
        print("Recolección de basura completada")

# Ejecutar el sistema
if __name__ == "__main__":
    system = NetworkMonitoringSystem(5)
    system.synchronize_clocks()
    system.monitor_network()
