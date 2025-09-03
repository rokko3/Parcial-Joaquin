grammar gramatica;


prog: fiboExpr EOF ;

fiboExpr: FIBO '(' INT ')' ;

FIBO: 'FIBO' ;
INT: [0-9]+ ;

WS: [ \t\r\n]+ -> skip ;
