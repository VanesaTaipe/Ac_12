#include <pthread.h>
#include <stdio.h>

pthread_mutex_t lock1 = PTHREAD_MUTEX_INITIALIZER;
pthread_mutex_t lock2 = PTHREAD_MUTEX_INITIALIZER;

void* function1(void* data) {
    pthread_mutex_lock(&lock1);
    printf("Hilo 1: ha adquirido lock1\n");
    pthread_mutex_lock(&lock2);
    printf("Hilo 1: ha adquirido lock2\n");
    pthread_mutex_unlock(&lock2);
    pthread_mutex_unlock(&lock1);
    return NULL;
}

void* function2(void* data) {
    pthread_mutex_lock(&lock2);
    printf("Hilo 2: ha adquirido lock2\n");
    pthread_mutex_lock(&lock1);
    printf("Hilo 2: ha adquirido lock1\n");
    pthread_mutex_unlock(&lock1);
    pthread_mutex_unlock(&lock2);
    return NULL;
}

int main() {
    pthread_t thread1, thread2;
    pthread_create(&thread1, NULL, function1, NULL);
    pthread_create(&thread2, NULL, function2, NULL);
    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);
    return 0;
}