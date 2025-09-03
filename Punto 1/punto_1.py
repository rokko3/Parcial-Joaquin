import sys

def automata(cadena):
    i = 0
    n = len(cadena)

    if n == 0:
        return True

    while i < n and cadena[i] == 'a':
        i += 1

    while i < n and cadena[i] == 'b':
        i += 1

    while i < n and cadena[i] == 'c':
        i += 1

    return i == n


def main():
    if len(sys.argv) != 2:
        print("No se ingreso un archivo de cadena")
        sys.exit(1)

    nombre_archivo = sys.argv[1]
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            cadena = linea.strip()
            print(f"{'Acepta' if automata(cadena) else 'No Acepta'}")


if __name__ == "__main__":
    main()
