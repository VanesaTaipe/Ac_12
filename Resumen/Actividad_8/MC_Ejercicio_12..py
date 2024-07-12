class CacheLine:
    def __init__(self):
        self.state = 'I'  # Initial state is Invalid
        self.value = None

    def read(self):
        if self.state == 'I':
            self.state = 'S'
            print("Transition to Shared")
        return self.value

    def write(self, value):
        if self.state in ('I', 'S'):
            self.state = 'M'
            print("Transition to Modified")
        self.value = value

    def get_state(self):
        return self.state

def main():
    cache_line = CacheLine()

    # Simulate write operation
    print("Writing value 42")
    cache_line.write(42)
    print(f"State after write: {cache_line.get_state()}")

    # Simulate read operation
    print("Reading value")
    value = cache_line.read()
    print(f"State after read: {cache_line.get_state()}")

if __name__ == "__main__":
    main()
