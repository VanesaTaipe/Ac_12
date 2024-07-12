class DistributedCache:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node_id):
        self.nodes[node_id] = {}

    def put(self, key, value):
        for node in self.nodes.values():
            node[key] = value

    def get(self, node_id, key):
        return self.nodes[node_id].get(key, None)

# Ejemplo de uso
cache = DistributedCache()
cache.add_node('node1')
cache.add_node('node2')

cache.put('key1', 'value1')
print(cache.get('node1', 'key1'))
print(cache.get('node2', 'key1'))