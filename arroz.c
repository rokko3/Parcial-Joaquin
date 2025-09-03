#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Uso: %s <archivo> <palabra_clave>\n", argv[0]);
        return 1;
    }

    char *nombre_archivo = argv[1];
    char *clave = argv[2];
    FILE *archivo = fopen(nombre_archivo, "r");

    if (!archivo) {
        perror("Error al abrir el archivo");
        return 1;
    }

    char linea[256];
    int contador = 0;

    while (fgets(linea, sizeof(linea), archivo)) {
        char *pos = linea;
        while ((pos = strstr(pos, clave)) != NULL) {
            int inicio_ok = (pos == linea || !isalnum(*(pos - 1)));
            int fin_ok = (*(pos + strlen(clave)) == '\0' || 
                          !isalnum(*(pos + strlen(clave))));
            
            if (inicio_ok && fin_ok) {
                contador++;
            }
            pos += strlen(clave);  
        }
    }

    fclose(archivo);

    printf("%s se repite %d veces en el texto.\n", clave, contador);

    return 0;
}
