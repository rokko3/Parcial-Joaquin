import re
import sys

# Definición de tokens y sus expresiones regulares
tokens = [
    ("SUMA", re.compile(r"^\+$")),
    ("INCR", re.compile(r"^\+\+$")),
    ("ENTERO", re.compile(r"^[0-9]+$")),
    ("REAL", re.compile(r"^[0-9]+\.[0-9]+$"))
]

def analizador_afd(cadena):
    for token, patron in tokens:
        if patron.match(cadena):
            return token
    return "ERROR"

def analizar_archivo(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        lineas = archivo.readlines()
    
    resultado = []
    for num_linea, linea in enumerate(lineas, start=1):
        palabras = linea.split()
        for palabra in palabras:
            token = analizador_afd(palabra)
            resultado.append((num_linea, palabra, token))
    
    return resultado

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python afd.py <archivo>")
        sys.exit(1)

    nombre_archivo = sys.argv[1]
    resultado = analizar_archivo(nombre_archivo)

    print("Tokens encontrados:\n")
    for linea, lexema, token in resultado:
        print(f"Línea {linea:3}  {lexema:10} → {token}")