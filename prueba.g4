
grammar prueba;
root : exprs             // l'etiqueta ja és root POSIBLEMENTE expr*
     ;

exprs : expr*
    ;
expr : '('ID params ')'          # expr_S //An expression is defined by a "ID" and a set of 0..n params
     | '('WORD params ')'        # expr_f
    ;
params : param*
    ;
param : NUM                 # number     //Param might be a number
     | WORD                 # var     //Param might be a word->variable already defined (also functions)
                                                //so far,  a var can just be a word...
                                                // we'll see about adding nums right after
     | expr                  # expr_param //Param also can be another expr (but as to be completetly one --> (read)
     ;

ID :  OPERATORS | CONDITIONAL | TRUE_FALSE;

OPERATORS: '+' | '-' | '*' | '/';
CONDITIONAL: '>'| '<' | '>=' | '<=' | '=' | '<>';
TRUE_FALSE: '#t' | '#f';

WORD: [a-zA-Z]+ ;
NUM : [0-9]+ ;
WS  : [ \t\n\r]+ -> skip ;



