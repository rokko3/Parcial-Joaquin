%{
#include <stdio.h>
#include <string.h>

int valido = 1;  
%}

NUM [0-9]+
DOUBLE [0-9]+ '.' [0-9]+
SPACE [ \t]+

%%

{ID}{SPACE}*={SPACE}*lambda{SPACE}+{ID}:{SPACE}*{ID}{SPACE}*\*{2}{SPACE}*{NUM}  
print\({ID}\({NUM}\)\)                                                            
{SPACE}+                                                                          
\n                                                                                
.                                                                                 

%%

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("No se ingreso un archivo para prueba");
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
