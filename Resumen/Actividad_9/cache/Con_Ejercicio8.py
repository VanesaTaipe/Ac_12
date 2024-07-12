class CacheLine:
    def __init__(self):
        self.state = 'Invalid'
        self.data = None
class Directory:
    def __init__(self):
        self.entries = {}

    def update(self, address, processor_id):
        if address not in self.entries:
            self.entries[address] = set()
        self.entries[address].add(processor_id)

    def invalidate(self, address):
        if address in self.entries:
            self.entries[address] = set()

class Processor:
    def __init__(self, id, directory):
        self.id = id
        self.cache = {}
        self.directory = directory

    def read(self, address):
        if address in self.cache and self.cache[address].state != 'Invalid':
            return self.cache[address].data
        else:
            self.cache[address] = CacheLine()
            self.cache[address].state = 'Shared'
            self.directory.update(address, self.id)
            self.cache[address].data = memory_read(address)
            return self.cache[address].data

    def write(self, address, data):
        if address in self.cache and (self.cache[address].state == 'Shared' or self.cache[address].state == 'Exclusive'):
            self.cache[address].state = 'Modified'
            self.cache[address].data = data
            self.directory.invalidate(address)
        else:
            self.cache[address] = CacheLine()
            self.cache[address].state = 'Modified'
            self.cache[address].data = data
            self.directory.invalidate(address)
            memory_write(address, data)

def memory_read(address):
    return "data_from_memory"

def memory_write(address, data):
    pass

# Ejemplo de uso
directory = Directory()
p1 = Processor(1, directory)
p2 = Processor(2, directory)
p1.write(0x1A, "data1")
p2.read(0x1A)
print(directory.entries)