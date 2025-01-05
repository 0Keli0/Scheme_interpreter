// Gramàtica per expressions senzilles
grammar lisp;
root : exprs             // l'etiqueta ja és root POSIBLEMENTE expr*
     ;

exprs : expr*
    ;
expr : '(' params ')'          # expr_S //An expression is defined by a "ID" and a set of 0..n params

    ;
params : param*
    ;
param : NUM                 # number     //Param might be a number
     | TRUE_FALSE           # boolean            //Param might be a word->variable already defined (also functions)
     | ID                   # var       //so far,  a var can just be a word...
     | STRING               # string
     | '\'' '(' params ')' # listElements                // we'll see about adding nums right after
     | expr                  # expr_param //Param also can be another expr (but as to be completetly one --> (read)
     ;


ID : WORD | OPERATORS | CONDITIONAL;


OPERATORS: '+' | '-' | '*' | '/';
CONDITIONAL: '>'| '<' | '>=' | '<=' | '=' | '<>';
TRUE_FALSE: '#t' | '#f';


STRING: '"'(~["\\] | '\\'.)*'"'; // Neigther " \\ or add whatever's afterward \\ as part of the string
WORD : [a-zA-Z_\u0080-\u00FF][a-zA-Z0-9_?-]* ; // Allows functions and variables names with "_" "-" numbers and "?"
NUM : [0-9]+ ('.' [0-9]+)?; // Integer and Floating Point
//FLOAT : [0-9]+ ('.' [0-9]+)? ; // Floating Point num
WS  : [ \t\n\r]+ -> skip ;
LINE_COMMENT: ';' ~[\r\n]* -> skip; // Single-line comments
MULTI_COMMENT: '#|' .*? '|#' -> skip; // Multi-line comments
//MULTI_COMMENT:
//  '#|'
//  ( '|'*? MULTI_COMMENT | ('|'* | ' '*) ~['|#])*
//  '|#'
//  -> skip;

//funtion: ('+' | '-' | '*' |'/' )      # simpleOperators
//     | ('>' | '<' | '<=' |'>=' )    # comparators
//     | 'define' '('WORD                     # function

//     |  WORD
//     | 'if' expr param param        # if
//     | 'cond'
//     |
//     ;
