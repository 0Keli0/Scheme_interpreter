# Mini Scheme Interpreter

## Introducción
Este proyecto está destinado a proveer un intérprete escrito en Python para Mini Scheme, un subconjunto del lenguaje de programación Scheme.

Este intérprete ha sido creado con motivos educativos basado en la práctica  GEI-LP (edició 2024-2025 Q1) `Pràctica LP: Mini Scheme`. 
Con motivo de ello, la implementación provista da soporte a un reducido conjunto de características propias del lenguaje propuesto.
Además, es una implementación propia, por lo que puede mostrar características no reflejadas en los estándares RnRS.


## Características Principales
### Evaluación de S-Expressions
El intérprete evalúa expresiones en formato S-Expression, que representan estructuras jerárquicas
del lenguaje Scheme, derivado de su primogénito Lisp. Este incluye:

- Soporte para operaciones aritméticas básicas (+, -, *, /) además de otras añadidas (mod, div)
- condicionales (<,>,=,<=,>=) y operaciones booleanas (and, or, not, #f, #t)
- Soporte para instrucciones condicionales (if, cond)
- Soporte para definir nuevas funciones y variables en tiempo de ejecución (define)
- Soporte para scope local (let)
- Soporte para operar y crear quoted-list inmutables (car, cdr, null?, '())
- Soporte para I/O (read, newline, display)
- Soporte para funciones como ciudadanos de primer orden
- Soporte para el manejo de algunos errores sintácticos

## Estructura del proyecto
- *scheme.py*: Archivo principal para ejecutar el intérprete desde terminal. 
- *Makefile*: Permite diferentes funcionalidades automatizadas para la generación pruebas, ejecutar el programa y hacer limpieza del proyecto. ^make^ hará un setup del entorno para poder ejecutar el programa
- *./interpreter_utils*: Código fuente donde se implementa la lógica del intérprete. Además, scheme.g4 es la gramática del lenguaje implementada para autogenerar las entradas con antlr.
  - *TreeParser.py*: Implementa la lógica necesaria para dar soporte al programa para que sus expresiones sean evaluadas y muestren el resultado esperado.
  - *TreeShow.py*: Implementación que nos muestra terminal el recorrido por terminal del árbol del programa ejecutado. 
  La función "evalProgram" con "show_visit_tree=1" permite mostrar el recorrido generado por "TreeShow.py". Manipulación desde *scheme.py*.
- *./scheme_programs*: Test de prueba con programas .scm para mostrar las cualidades del intérprete
- *./inout*: Directorio con los diferentes archivos necesarios para el input/output de los programas scheme dados como ejemplo


## Librerías
Las librerías utilizadas son las que se presentarán a continuación (en caso de ser necesario instalarlas, estarán presentes en `requiremnts.txt`):
- antlr4: Herramienta utilizada para generar el analizador léxico y sintáctico a partir de una gramática. En este caso, la gramática `scheme.g4` define la sintaxis de Mini Scheme.
- copy: Para copias parciales donde la copia superficial se tiene presente

## Instrucciones de uso
### Makefile
El makefile contiene una serie de comandos que permite la instrumentación del proyecto completo. Sin embargo, la instrucción all está encomendada a hacer 
un setup con el ".jar" de antlr que encontramos en la carpeta de "interpreter_utils", junto a la instalación de algunas dependencias necesarias. 
Además, nos mostrará una serie de opciones que el makefile contiene para poder generar los tests y ejecutar el programa "all.scm". Entre ellas podemos encontrar:
- run: Ejecuta programa "all.scm" que contiene todos los programas en un solo archivo
- antlr: Vuelve a generar parser y lexer de antlr por si hay algún cambio en la gramática tras el setup
- clean: Elimina los archivos autogenerados por antlr, la parpeta output_files y la caché de python
- generate_tests: Ejecución de todos los programas test implementados

### Uso
En el caso en el que queramos ejecutar un programa tras hacer setup del entorno, lo podremos hacer de la siguiente forma:
```bash
python3 scheme.py ./scheme_programs/example_test.scm < ./inout/input_files/example_input.txt > ./inout/input_files/example_output.txt
```
Los nombres de los archivos input y output comienzan por el nombre de sus respectivos test seguidos de "_input.txt" o "_output.txt" respectivamente.
Por ejemplo:
```bash
python3 scheme.py ./scheme_programs/*repo_main_features1_test*.scm < ./inout/input_files/*repo_main_features1_test*_input.txt > ./inout/input_files/*repo_main_features1_test*_output.txt
```

## Gramática
La gramática utilizada en este intérprete para scheme muestran gran sencillez. Esto se ve debido a que scheme se compone de listas
donde el primer elemento es una función, y los siguientes posibles elementos son sus argumentos. 

```scheme
(func arg1 arg2 ...)
```

Esto hará que en nuestra gramática se componga de un conjunto de expresiones, donde cada expresión se compondrá de una lista donde internamente tenga
un conjunto de 0 a n parámetros.

```g4
expr : '(' params ')'          # expr_S         //An expression defined by a set of 0..n params
    ;
```
Cada parámetro podrá ser un conjunto reducido de elementos. Entre ellos encontramos números, booleanos, funciones/variables, cadenas de texto, quoted-list y más expresiones

```g4
param : NUM                 # number            //Número entero o real
     | TRUE_FALSE           # boolean           //#t o #f
     | ID                   # var               //Funciones o variables
     | STRING               # string            //Cadenas expresadas entre " "
     | '\'' '(' params ')' # listElements       //Lista como quoted-list '()
     | expr                  # expr_param       //Expresión anidada
     ;
```
Para finalizar, se han implementado la asignación de comentarios de una línea y multilínea, para poder comentar y depurar con mayor facilidad

```g4
LINE_COMMENT: ';' ~[\r\n]* -> skip;             // Single-line comment -->  ;
MULTI_COMMNET: '#|' .*? '|#' -> skip;           // Multi-line comment -->  #| and |#
```

## Programas Scheme 
Se han implementado un set de pruebas para mostrar diferentes características del intérprete. Estos tests son un conjunto de 10 módulos divididos en 5 programas diferentes.

-<*repo_main_features1_test.scm*> Módulos 1-3: Implementación similar de los ejemplos propuestos del repositorio de la práctica junto a añadidos
  - Módulo 1: Implementación de operaciones básicas
  - Módulo 2: Uso de `define` para funciones básicas y constantes junto a la implementación de instrucciones condicionales `if` y `cond`.
  - Módulo 3: Manipulación de listas `'()` con sus diferentes funciones.
-<*repo_main_features2_test.scm*> Módulos 4-7: Continuación de las características a mostrar por la práctica.
  - Módulo 4: 3 definiciones de funciones recursivas
  - Módulo 5: Ejemplo de scope local utilizando `let`
  - Módulo 6: Ejemplo I/O para mostrar la posibilidad de introducir cadenas de texto como input
  - Módulo 7: 4 ejemplos de funciones pasadas como parámetro. Entre ellas encontramos dos ejemplos de map, donde en el segundo ejemplo pasamos como parámetro
    una función la cual utiliza otra función pasada como parámetro. 

-<*laziness_aware_test.scm*> Módulo 8: Mostramos cómo `define` no evalúa la asignación hasta que sea necesaria utilizar la variable,
  mientras que el caso de `let` para variables evaluamos directamente la asignación dada. Esto nos permitirá tener diversos comportamientos
  según lo que busquemos.

-<*scope_test.scm*> Módulo 9: Demostramos cómo las variables definidas por `let` son únicamente alcanzables por el scope en el que se definieron.
  Por otro lado, define tiene un scope dinámico, por lo que podremos acceder a funciones y variables de manera global siempre y cuando hayan sido previamente definidas.

-<*error_checkers.scm*> Módulo 10: Mostramos el funcionamiento de los diferentes checkers implementados para errores de sintáxis según el operador a evaluar.
  Es importante comentar que la implementación actual está dispuesta para que simplemente muestre estos errores y trate de continuar con la ejecución. La intención de ello
  es poder mostrar diversos ejemplos de error a la vez. Para que muestre la traza de errores correctamente, además de la excepción lanzada solo habría que descomentar la línea `raise` 
  en la función `raiseError(msg)` implementada en TreeParser.py. 
  Aun teniendo esto presente, existen errores que siguen interrumpiendo el transcurso de ejecución debido a que la lógica de evaluación está conscientemente implementada con una sintáxis correcta.
  Por ello, hay ciertos ejemplos comentados en este programa, los cuales habría que descomentar para observar dichas partes del código. 
  Finalmente, comentar que, al presentar una sintaxis sencilla es fácil de evaluar cuando se requieren más argumentos de los encontrados. Sin embargo, al hacer lo posible por evaluar lo estrictamente 
  necesario, podemos encontrar errores de sintaxis que no serían lanzados por la lógica y, por lo tanto, por python. Esto es lo que se pretende mostrar, por ejemplo, con el error lanzado con `if` de la forma:
```scheme
  (display "(if C, N1, N2, N3) -> ") (if #t 1 2 3)
```
  Debido a que `else` únicamente evaluará el segundo argumento, no se tendrá constancia de si existe alguna continuación a no ser que sea comprobado. Esta es la razón por la que se puede continuar la ejecución
  del programa sin presentar más errores.

