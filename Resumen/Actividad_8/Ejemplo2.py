#Ejercicio 2: Paralelización de operaciones matriciales con NumPy y Joblib

#Descripción: Paraleliza una serie de operaciones matriciales (multiplicación de matrices)
#utilizando Joblib.

#Tareas:
#Crear dos matrices grandes con numpy.
#Dividir las matrices en sub-matrices.
#Multiplicar las sub-matrices en paralelo utilizando Joblib.
#Reunir los resultados y formar la matriz resultante.

#Pistas:
#Usa numpy.split para dividir las matrices.
#Usa joblib.Parallel y joblib.delayed para el procesamiento paralelo.

import numpy as np
from joblib import Parallel, delayed


def multiply_sub_matrices(A, B):
    return np.dot(A, B)


def parallel_matrix_multiplication():
    #Se crean las dos matrices, con valores aleatorios de una distribución normal (valores de [0,1)), de 1000x1000
    A = np.random.rand(1000, 1000)
    B = np.random.rand(1000, 1000)

    #Se divide cada una de las matrices en 4 segmentos
    A_subs = np.array_split(A, 4, axis=0) #1000/4=250 "elementos" por sección--> axis=0 implica que habrán 250 filas
    #print(np.array(A_subs).shape) 4 segmentos, de 250x1000

    B_subs = np.array_split(B, 4, axis=1) #1000/4=250 --> axis=1 implica 250 columnas
    #print(np.array(A_subs).shape) 4 segmentos, de 1000x250


    #Para comprobar ello, veamos el "shape" de las submatrices de la posición "0":
    # print(A_subs[0].shape)
    # print(B_subs[0].shape)
    #Lo que genera --> (250,1000), (1000,250) --> Eso implica que se están creando matrices
    #más pequeñas con el objetivo de realizar el producto matricial, pues para realizar dicha operación
    #es necesario que las matrices sean de la forma (m*n)(n*l), lo cual cumple. De esta manera,
    #se realizará la multiplicación de matrices de forma paralela en los 4 segmentos creados

    #Como son 4 segmentos sobre los que se deben operar, se crearán, entonces, 4 instancias de la clase "Parallel"
    results = Parallel(n_jobs=4)(delayed(multiply_sub_matrices)(A_sub, B_sub) for A_sub in A_subs for B_sub in B_subs)


    #La función "delayed", lo que realmente permite hacer, es decirle a Python qué funciones queremos
    #llamar con qué argumentos, sin realmente llamarlas. En otras palabras, queremos retrasar la ejecución.
    #Por lo que si se ejecuta, solamente, lo siguiente, se tiene como resultado un "generador":
    #Pues los generadores siguen el principio de "lazy evaluation":
    #print(delayed(multiply_sub_matrices)(A_sub, B_sub) for A_sub in A_subs for B_sub in B_subs)

    #Sin embargo, de manera resumida, se está pasando a cada una de las instancias "parallel", cada
    #una de las submatrices anteriormente creadas

    #Acá, se crea una matríz de 0, para posteriormente colocarse sobre esa matriz, los
    #resultados calculados por cada una de las submatrices y así tener el resultado total
    #de la multiplicación matricial

    C = np.zeros((1000, 1000))
    for i in range(4):
      for j in range(4):
            C[i*250:(i+1)*250, j*250:(j+1)*250] = results[i*4+j]
#Cada sub-matriz resultante se asigna a la porción correspondiente de C utilizando la indexación C[i*250:(i+1)250, j250:(j+1)250] = results[i4+j].

#i*250 y (i+1)*250 representan los límites de las filas de la porción de C donde se asignará la sub-matriz resultante.
#j*250 y (j+1)*250 representan los límites de las columnas de la porción de C donde se asignará la sub-matriz resultante.
#results[i*4+j] accede a la sub-matriz resultante correspondiente en la lista results.
    return C

C = parallel_matrix_multiplication()
print(C)
print(C.shape)
