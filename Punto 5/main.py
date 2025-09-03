import sys

def fibonacci(n):
    """Genera la secuencia de Fibonacci hasta n términos."""
    secuencia = [0, 1]
    while len(secuencia) < n:
        secuencia.append(secuencia[-1] + secuencia[-2])
    return secuencia[:n]

def main():
    if len(sys.argv) != 2:
        print("Uso: python main.py <numero>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n <= 0:
            print("Ingrese un número mayor que 0")
            sys.exit(1)
    except ValueError:
        print("El argumento debe ser un número entero")
        sys.exit(1)

    resultado = fibonacci(n)
    print(f"Fibonacci de {n}: {resultado}")

if __name__ == "__main__":
    main()
