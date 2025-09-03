%{
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

void yyerror(const char *s);
int yylex();
extern FILE *yyin;
%}

%union {
    double num;
}

%token <num> NUM
%token SQRT
%token EOL

%type <num> expr

%%

input:
    | input line
    ;

line:
    expr EOL   { printf("Resultado: %.4f\n", $1); }
    | EOL
    ;

expr:
    NUM                  { $$ = $1; }
    | SQRT '(' expr ')'  { 
                            if ($3 < 0) {
                                $$ = 0;
                            } else {
                                $$ = sqrt($3);
                            }
                         }
    ;

%%
void yyerror(const char *s) {
  printf("No se puede calcular la raiz de un numero negativo o incluir caracteres no valido");
}

int main(int argc, char **argv) {
    if (argc != 2) {
        printf("Ingrese un archivo");
        exit(1);
    }

    FILE *f = fopen(argv[1], "r");
    if (!f) {
        perror("No se pudo abrir el archivo");
        exit(1);
    }

    yyin = f;
    yyparse();
    fclose(f);
    return 0;
}
