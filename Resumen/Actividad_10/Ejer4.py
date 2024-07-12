counter = 0
lock = threading.Lock()

def unsafe_update():
    global counter
    local_copy = counter
    local_copy += 1
    time.sleep(0.1)  # Simular carga de trabajo
    counter = local_copy

def safe_update():
    global counter
    with lock:
        local_copy = counter
        local_copy += 1
        time.sleep(0.1)  # Simular carga de trabajo
        counter = local_copy

# Cambiar safe_update por unsafe_update para ver el efecto de una condición de carrera
update_thread1 = threading.Thread(target=safe_update)
update_thread2 = threading.Thread(target=safe_update)
update_thread1.start()
update_thread2.start()
update_thread1.join()
update_thread2.join()
print("Valor final del contador:", counter)
