traffic = 0

class CacheLine:
    def __init__(self):
        self.state = 'Invalid'
        self.data = None

class Processor:
    def __init__(self, id):
        self.id = id
        self.cache = {}

    def read(self, address):
        global traffic
        if address in self.cache and self.cache[address].state != 'Invalid':
            return self.cache[address].data
        else:
            self.cache[address] = CacheLine()
            self.cache[address].state = 'Shared'
            traffic += 1
            self.cache[address].data = memory_read(address)
            return self.cache[address].data

    def write(self, address, data):
        global traffic
        if address in self.cache and (self.cache[address].state == 'Shared' or self.cache[address].state == 'Exclusive'):
            self.cache[address].state = 'Modified'
            self.cache[address].data = data
        else:
            self.cache[address] = CacheLine()
            self.cache[address].state = 'Modified'
            traffic += 1
            self.cache[address].data = data
            memory_write(address, data)

def memory_read(address):
    return "data_from_memory"

def memory_write(address, data):
    pass

# Ejemplo de uso
p1 = Processor(1)
p2 = Processor(2)
p1.write(0x1A, "data1")
p2.read(0x1A)
print(f"Traffic: {traffic} transactions")