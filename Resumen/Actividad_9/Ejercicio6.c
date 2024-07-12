#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
/*Implementa la suma de dos vectores grandes distribuidos entre varios nodos utilizando MPI en C.*/
int main(int argc, char** argv) {
    MPI_Init(&argc, &argv);

    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    int vector_size = 1000000;
    int local_size = vector_size / size;

    double* local_A = (double*)malloc(local_size * sizeof(double));
    double* local_B = (double*)malloc(local_size * sizeof(double));
    double* local_C = (double*)malloc(local_size * sizeof(double));
    /*e utiliza para asignar un bloque de memoria en el montón.
    proporciona la cantidad de almacenamiento,*/
    for (int i = 0; i < local_size; i++) {
        local_A[i] = rank + 1;
        local_B[i] = rank + 2;
    }

    MPI_Allreduce(local_A, local_C, local_size, MPI_DOUBLE, MPI_SUM, MPI_COMM_WORLD);
    /*Realiza una operación de reducción en todos los procesos y devuelve el resultado a todos los procesos. En este caso, suma todos los elementos de `local_A` y almacena el resultado en `local_C`.*/

    for (int i = 0; i < local_size; i++) {
        local_C[i] = local_A[i] + local_B[i];
    }

    free(local_A);
    free(local_B);
    free(local_C);

    MPI_Finalize();
    return 0;
}
/*mpicc Ejercicio6.c -o Ejercicio6*/
