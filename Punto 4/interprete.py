import time
import psutil
import os

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def get_memory_usage():

    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 

def main():
    n = 100
    
    print("Consumo de ram en python: ")
    
    mem_inicio = get_memory_usage()
    print(f"Memoria inicial: {mem_inicio:.2f} KB")

    start_time = time.time()
    resultado = fibonacci(n)
    end_time = time.time()
    
    mem_fin = get_memory_usage()
    tiempo_ejecucion = end_time - start_time
    
    print(f"Fibonacci({n}) = {resultado}")
    print(f"Tiempo ejecucion: {tiempo_ejecucion:.4f} s")
    print(f"Memoria usada: {mem_fin - mem_inicio:.2f} KB")
    print(f"Memoria usada: {(mem_fin - mem_inicio) / 1024:.2f} MB")



if __name__ == "__main__":
    main()