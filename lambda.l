%{
#include <stdio.h>
#include <string.h>

int valido = 1;   // bandera para indicar si la expresión es válida
%}

/* Definición de expresiones regulares */
ID          [a-zA-Z_][a-zA-Z0-9_]*
NUM         [0-9]+
SPACE       [ \t]+

%%

{ID}{SPACE}*={SPACE}*lambda{SPACE}+{ID}:{SPACE}*{ID}{SPACE}*\*{2}{SPACE}*{NUM}  
print\({ID}\({NUM}\)\)                                                            
{SPACE}+                                                                          
\n                                                                                
.                                                                                 

%%

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Uso: %s <archivo>\n", argv[0]);
        return 1;
    }

    FILE *archivo = fopen(argv[1], "r");
    if (!archivo) {
        perror("No se pudo abrir el archivo");
        return 1;
    }

    yyin = archivo;
    yylex();
    fclose(archivo);

    if (valido)
        printf("ACEPTA\n");
    else
        printf("NO ACEPTA\n");

    return 0;
}

int yywrap() {
    return 1;
}
