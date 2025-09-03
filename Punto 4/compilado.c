#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/resource.h>

long get_memory_usage_kb() {
    struct rusage usage;
    getrusage(RUSAGE_SELF, &usage);
    #ifdef __APPLE__
        return usage.ru_maxrss / 1024;  // macOS devuelve bytes
    #else
        return usage.ru_maxrss;         // Linux devuelve KB
    #endif
}

long long fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n-1) + fibonacci(n-2);
}

int main() {
    int n = 42;
    
    printf("=== CONSUMO DE RAM - C (Compilado) ===\n");
    
    long mem_inicio = get_memory_usage_kb();
    printf("Memoria inicial: %ld KB\n", mem_inicio);
    
    clock_t start = clock();
    long long resultado = fibonacci(n);
    clock_t end = clock();
    
    long mem_fin = get_memory_usage_kb();
    double tiempo = ((double)(end - start)) / CLOCKS_PER_SEC;
    
    printf("Fibonacci(%d) = %lld\n", n, resultado);
    printf("Tiempo ejecución: %.4f s\n", tiempo);
    printf("Memoria final: %ld KB\n", mem_fin);
    printf("Memoria usada: %ld KB\n", mem_fin - mem_inicio);
    printf("Memoria usada: %.2f MB\n", (mem_fin - mem_inicio) / 1024.0);
    
    return 0;
}