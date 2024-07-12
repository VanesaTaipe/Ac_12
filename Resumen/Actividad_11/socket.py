import socket

def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 12345))
    s.listen(1)
    conn, addr = s.accept()
    print('Connected by', addr)
    data = conn.recv(1024)
    print('Received', data)
    conn.close()

def client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 12345))
    s.sendall(b'Hello, world')
    s.close()

if __name__ == "__main__":
    from multiprocessing import Process
    p1 = Process(target=server)
    p2 = Process(target=client)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
