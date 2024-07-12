class Node:
    def __init__(self, id):
        self.id = id
        self.data = {}
        self.log = []

    def put(self, key, value):
        self.data[key] = value
        self.log.append((key, value))

    def get(self, key):
        return self.data.get(key, None)

    def replicate(self, other_node):
        for entry in self.log:
            other_node.data[entry[0]] = entry[1]
        other_node.log.extend(self.log)

# Ejemplo de uso
node1 = Node('node1')
node2 = Node('node2')

node1.put('key1', 'value1')
node1.put('key2', 'value2')

node1.replicate(node2)

print(node2.get('key1'))
print(node2.get('key2'))