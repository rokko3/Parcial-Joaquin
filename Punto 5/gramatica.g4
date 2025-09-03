grammar gramatica;

prog: expr EOF ;

expr
    : 'fibo' '(' NUM ')'   #fibo
    | NUM                  #number
    ;

NUM: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;
