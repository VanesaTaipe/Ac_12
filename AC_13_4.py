from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

N = 1024
local_N = N // size

if rank == 0:
    vector = np.random.rand(N)
else:
    vector = None

local_vector = np.zeros(local_N)
comm.Scatter(vector, local_vector, root=0)

local_sum = np.sum(local_vector)
total_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)

if rank == 0:
    print(f"Suma total: {total_sum}")




#El overhead de comunicación se refiere al tiempo adicional requerido para coordinar y transferir datos entre procesadores en un sistema paralelo, puede ser un factor limitante significativo en el rendimiento del paralelismo. 
#

# `comm.Scatter` y `comm.reduce`, que distribuyen los datos del vector entre los #procesadores y luego suman los resultados locales, respectivamente.
#Este overhead se refiere al tiempo adicional que se necesita para coordinar y transferir datos entre procesadores. Si el overhead de comunicación es alto, puede limitar la eficiencia del algoritmo, incluso si el algoritmo en sí es altamente paralelizable.
#El overhead de comunicación puede cambiar con el aumento del número de procesadores. En general, a medida que aumenta el número de procesadores, también lo hace el overhead de comunicación. 
