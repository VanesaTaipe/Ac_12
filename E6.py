#Este ejemplo en Python implementa un algoritmo de búsqueda paralela utilizando #comunicaciones no bloqueantes y grupos.
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# Definir el tamaño del problema
N = 100000
sub_size = N // size

# Inicializar datos
if rank == 0:
    data = np.random.randint(0, 100, N)
    target = np.random.randint(0, 100)
else:
    data = None
    target = None

# Broadcast del target a todos los procesos
#La función de difusión (broadcast) permite enviar un mensaje desde un proceso a todos los demás procesos en un grupo. Esto es útil cuando un nodo necesita distribuir datos a todos los otros nodos
target = comm.bcast(target, root=0)

# Scatter de los datos a los procesos
sub_data = np.empty(sub_size, dtype='i')
comm.Scatter(data, sub_data, root=0)

# Búsqueda en el subconjunto de datos
found_indices = np.where(sub_data == target)[0]

# Recolectar resultados
all_found_indices = comm.gather(found_indices, root=0)

if rank == 0:
    all_found_indices = np.concatenate(all_found_indices)
    print(f"Índices encontrados del objetivo ({target}): {all_found_indices}")
#Broadcast del objetivo: El valor objetivo de búsqueda se distribuye a todos los procesos utilizando comm.bcast.
# Scatter de datos: Los datos se dividen entre los procesos utilizando comm.Scatter.
# Búsqueda local: Cada proceso busca el valor objetivo en su subconjunto de datos.
#Gather de resultados: Los índices encontrados se recopilan en el proceso raíz utilizando
