#include <stdio.h>
#include <unistd.h>

int main() {
    int fd[2];
    pipe(fd);
    pid_t pid = fork();

    if (pid == 0) {
        // Proceso hijo
        close(fd[0]);
        char message[] = "Hello from child";
        write(fd[1], message, sizeof(message));
        close(fd[1]);
    } else {
        // Proceso padre
        close(fd[1]);
        char buffer[100];
        read(fd[0], buffer, sizeof(buffer));
        printf("%s\n", buffer);
        close(fd[0]);
    }
    return 0;
}