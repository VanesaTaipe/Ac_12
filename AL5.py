import time

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
        next_node_id = self.request_queue.pop(0)
        next_node = [node for node in nodes if node.node_id == next_node_id][0]
        self.send_token(next_node)

    def enter_critical_section(self):
        print(f"Nodo {self.node_id} ingresando a la seccion critica")
        # Critical section code here
        self.leave_critical_section()

    def leave_critical_section(self):
        print(f"Nodo {self.node_id} dejando critical section")
        if self.request_queue:
            self.send_token_to_next_in_queue()

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
            addr = obj
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




server = CristianServer()
client = CristianClient(server)
client.synchronize_clock()
print(client.time)

nodes = [RaymondMutex(i) for i in range(3)]
nodes[0].parent = nodes[1]
nodes[1].parent = nodes[2]


nodes[0].request_access()
time.sleep(2)
nodes[0].leave_critical_section()
collector = MarkCompactCollector(len(nodes))
addr1 = collector.allocate("obj1")
print(f"Asignado el obj1 en: {addr1}")
collector.collect()
print("Recoleccion de basura completa")
