// Scheme Grammar
grammar scheme;
root : exprs                                    // root label
     ;
exprs : expr*
    ;
expr : '(' params ')'          # expr_S         //An expression defined by a set of 0..n params
    ;
params : param*
    ;
param : NUM                 # number            //Param as a number
     | TRUE_FALSE           # boolean           //Param as a boolean
     | ID                   # var               //Param as either variable or a function
     | STRING               # string            //Param as a string
     | '\'' '(' params ')' # listElements       //Param as a quoted list
     | expr                  # expr_param       //Param also can be another expr (but as to be completetly one --> (read))
     ;

ID : WORD | OPERATORS | CONDITIONAL;            //ID recognise a label that the interpreter will save with a purpose


OPERATORS: '+' | '-' | '*' | '/';
CONDITIONAL: '>'| '<' | '>=' | '<=' | '=' | '<>';
TRUE_FALSE: '#t' | '#f';


STRING: '"'(~["\\] | '\\'.)*'"';                // Neigther "\\ or add whatever is afterward \\ as part of the string
WORD : [a-zA-Z_\u0080-\u00FF][a-zA-Z0-9_?-]* ;  // Allows functions and variables names with: "_","-", numbers and "?"
NUM : '-'?[0-9]+ ('.' [0-9]+)? ;                // Integer and Floating Point
WS  : [ \t\n\r]+ -> skip ;
LINE_COMMENT: ';' ~[\r\n]* -> skip;             // Single-line comment
MULTI_COMMNET: '#|' .*? '|#' -> skip;           // Multi-line comment
