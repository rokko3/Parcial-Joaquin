#include <stdio.h>
#include <time.h>

long long factorial_c(int n) {
    if (n == 0) {
        return 1;
    } else {
        return n * factorial_c(n - 1);
    }
}

int main() {
    clock_t start_time, end_time;
    double cpu_time_used;
    long long result;

    start_time = clock();
    result = factorial_c(100);
    end_time = clock();
    cpu_time_used = ((double) (end_time - start_time)) / CLOCKS_PER_SEC;

    printf("Tiempo de ejecucion: %f seconds\n", cpu_time_used);

    return 0;
}