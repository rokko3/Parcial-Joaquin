import sys
def automata(cadena):

    funciona = 0
    for i, c in enumerate(cadena):
        if i==0:
            if primercaractervalido(c):
                funciona=1
            else:
                return False

        if ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9'):
            funciona=1
        else:
            funciona=0


    return funciona==1
def primercaractervalido(c):

    if ('a' <= c <= 'z') or ('A' <= c <= 'Z'):
        return True
    else:
        return False

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
