# Mini Scheme Interpreter

## Introducción
Este proyecto está destinado a proveer un intérprete escrito en Python para Mini Scheme, un subconjunto del lenguaje de programación Scheme.

Este intérprete ha sido creado con motivos educativos, basándose en la práctica  `GEI-LP (edició 2024-2025 Q1)` `Pràctica LP: Mini Scheme`. 
Con motivo de ello, la implementación provista da soporte a un reducido conjunto de características propias del lenguaje propuesto.
Además, es una implementación propia, por lo que puede mostrar características no reflejadas en los estándares `RnRS`.


## Características Principales
### Evaluación de S-Expressions
El intérprete evalúa expresiones en formato `S-Expression`, que representan estructuras jerárquicas
del lenguaje Scheme derivadas de su antecesor, Lisp. 

Las características principales que este intérprete incluye son:

- Soporte para operaciones aritméticas básicas (+, -, *, /), además de otras añadidas (mod, div)
- condicionales (<,>,=,<=,>=) y operaciones booleanas (and, or, not, #f, #t)
- Soporte para instrucciones condicionales (if, cond)
- Soporte para definir nuevas funciones y variables en tiempo de ejecución (define).
- Soporte para scope local (let)
- Soporte para redefinir funciones y variables
- Soporte para operar y crear quoted-list inmutables (car, cdr, null?, '())
- Soporte para I/O (read, newline, display)
- Soporte para funciones como ciudadanos de primer orden
- Soporte para el manejo de algunos errores sintácticos

## Estructura del proyecto
- ***scheme.py***: Archivo principal para ejecutar el intérprete desde terminal. 
- ***Makefile***: Permite crear el entorno necesario para la evaluación de programas `.scm`.
- ***./interpreter_utils***: Código fuente donde se implementa la lógica del intérprete. Además, scheme.g4 es la gramática del lenguaje implementada para autogenerar las entradas con antlr.
  - ***TreeEvaluator.py***: Contiene la lógica necesaria para dar soporte al programa, permitiendo que sus expresiones sean evaluadas y muestren el resultado esperado.
  - ***TreeShow.py***: Implementación que nos muestra el recorrido por terminal del árbol del programa ejecutado. 
  La función _evalProgram_ con _show_visit_tree=1_ permite mostrar el recorrido generado por _TreeShow.py_. Manipulación desde *scheme.py*.
  - ***antlr-4.13.2-complete.jar***: Jar con el que generamos los archivos necesarios para el parser y el lexer.
- ***./scheme_programs***: Test de prueba con programas `.scm` para mostrar las cualidades del intérprete
- ***./inout***: Directorio con los diferentes archivos necesarios para el input/output de los programas scheme dados como ejemplo


## Librerías
Las librerías utilizadas son las que se presentarán a continuación:
- *antlr4*: Herramienta utilizada para generar el analizador léxico y sintáctico a partir de una gramática. En este caso, la gramática `scheme.g4` define la sintaxis de Mini Scheme.
- *copy*: Nos permite hacer copias parciales de ciertas estructuras de datos. En estos casos se ha utilizado el método `copy.copy()`, tenido presente que este hace una copia superficial de ciertas estructuras más complejas contenidas en otras.

## Instrucciones de uso
### Makefile
El `Makefile` del proyecto contiene las funciones necesarias para poder hacer un setup del entorno y poder utilizar el intérprete.
Además, la instrucción `clean` permite hacer limpieza del código autogenerado por antlr, los archivos test_output.txt y la caché de python.

Como añadidos, podemos encontrar las siguientes instrucciones:
- `make generate_tests`: Permite la generación y comparación automática de todos los programas dentro de la carpeta `./scheme_programs`
- `make run`: Ejecuta el intérprete para el programa `all.scm`, el cual contiene todos los programas en uno.
- `make antlr`: Genera el parser y el lexer por medio del comando `antlr4`. Con el motivo de asegurar el correcto funcionamiento del intérprete, el setup se realiza ejecutando con `java` el archivo `antlr-4.13.2-complete.jar` .

### Uso
Primero, deberemos hacer `make` para autogenerar los `Visitors` autogenerados por antlr y la gramática dada. Después, deberemos de utilizar el _main_ `scheme.py` para ejecutar cualquiera de los programas `.scm` que encontremos en la 
carpeta `./scheme_programs`. Además, tendremos que redirigir la entrada y salida estándar a los `.txt` correspondientes en el caso de utilizar los programas propuestos.
```bash
make
python3 scheme.py ./scheme_programs/example_test.scm < ./inout/input_files/example_input.txt > ./inout/input_files/example_output.txt
```
Los nombres de los archivos input y output comienzan por el nombre de sus respectivos test seguidos de __input.txt_ u __output.txt_, respectivamente.
Por ejemplo:
```bash
python3 scheme.py ./scheme_programs/*repo_main_features1_test*.scm < ./inout/input_files/*repo_main_features1_test*_input.txt > ./inout/input_files/*repo_main_features1_test*_output.txt
```

## Gramática
La gramática utilizada en el intérprete muestran una gran sencillez. Esto se ve debido a que Scheme dispone su código de la misma manera que una de sus estructuras 
de datos: en *listas*. Estas expresiones presentan un primer elemento que define a una función, continuada de sus argumentos. 

```scheme
(func arg1 arg2 ...)
```

Para simplificar aún más la gramática, se decidió que estas expresiones que compondrán de un conjunto de parámetros.
```g4
expr : '(' params ')'          # expr_S         //An expression defined by a set of 0..n params
    ;
```
Cada parámetro podrá ser un elemento conjunto reducido de valores y expresiones. Entre ellos encontramos: números, booleanos, funciones/variables, cadenas de texto, quoted-list y más expresiones

```g4
param : NUM                 # number            //Número entero o real
     | TRUE_FALSE           # boolean           //#t o #f
     | ID                   # var               //Funciones o variables
     | STRING               # string            //Cadenas expresadas entre " "
     | '\'' '(' params ')' # listElements       //Lista como quoted-list '()
     | expr                  # expr_param       //Expresión anidada
     ;
```
Para finalizar, se han implementado la asignación de comentarios de una línea y multilínea para facilitar la compresión del código y depurar con mayor facilidad

```g4
LINE_COMMENT: ';' ~[\r\n]* -> skip;             // Single-line comment -->  ;
MULTI_COMMNET: '#|' .*? '|#' -> skip;           // Multi-line comment -->  #| and |#
```

## Programas Scheme 
Se ha implementado un set de pruebas para mostrar diferentes características del intérprete. Estos tests son un conjunto de 10 módulos divididos en 5 programas diferentes.

- <***repo_main_features1_test.scm***> Módulos 1-3: Implementación similar de los ejemplos propuestos del repositorio de la práctica junto a añadidos
  - Módulo 1: Implementación de operaciones básicas
  - Módulo 2: Uso de `define` para funciones básicas y constantes junto a la implementación de instrucciones condicionales `if` y `cond`.
  - Módulo 3: Uso de listas `'()` con sus diferentes funciones específicas.
- <***repo_main_features2_test.scm***> Módulos 4-7: Continuación de las características a mostrar por la práctica.
  - Módulo 4: 3 definiciones de funciones recursivas
  - Módulo 5: Ejemplo de scope local utilizando `let`
  - Módulo 6: Ejemplo I/O para mostrar la posibilidad de introducir cadenas de texto como input
  - Módulo 7: 4 ejemplos de funciones pasadas como parámetro. Entre ellas encontramos dos ejemplos de map, donde en el segundo ejemplo pasamos como parámetro
    una función la cual utiliza otra función pasada como parámetro. 

- <***laziness_aware_test.scm***> Módulo 8: Mostramos cómo `define` no evalúa la asignación hasta que sea necesaria utilizar la variable,
  mientras que el caso de `let` para variables evaluamos directamente la asignación dada. Esto nos permitirá tener diversos comportamientos
  según lo que busquemos.

- <***scope_test.scm***> Módulo 9: Demostramos cómo las variables definidas por `let` son únicamente alcanzables por el scope en el que se definieron.
  Por otro lado, define tiene un scope dinámico, por lo que podremos acceder a funciones y variables de manera global siempre y cuando hayan sido previamente definidas.

- <***error_checkers.scm***> Módulo 10: Se muestra el funcionamiento de los diferentes checkers implementados para errores de sintáxis según el operador a evaluar. 
  Es importante comentar que la implementación actual está dispuesta para que simplemente muestre estos errores y trate de continuar con la ejecución. La intención de ello
  es poder mostrar diversos ejemplos de error a la vez. Para que muestre la traza de errores correctamente, además de la excepción lanzada, solo habría que descomentar la línea `raise` 
  en la función `raiseError(msg)` implementada en TreeEvaluator.py. 
  Aun teniendo esto presente, existen errores que siguen interrumpiendo el transcurso de ejecución debido a que la lógica de evaluación está conscientemente implementada para una sintáxis correcta.
  Por ello, hay ciertos ejemplos comentados en este programa los cuales habría que descomentar para observar dichas partes del código. 
  Finalmente, comentar que, al presentar una sintaxis sencilla es fácil de evaluar cuando se requieren más argumentos de los encontrados. Sin embargo, al tratar de hacer lo posible por evaluar lo estrictamente 
  necesario, podemos encontrar errores de sintaxis que no serían lanzados por la lógica de la implementación y, por lo tanto, por python. Esto es lo que se pretende mostrar, por ejemplo, con el error lanzado con `if` de la forma:

    ```scheme
      (display "(if C, N1, N2, N3) -> ") (if #t 1 2 3)
    ```
  Debido a que `else` únicamente evaluará el segundo argumento, no se tendrá constancia de si existe alguna continuación a no ser que sea comprobado. Esta es la razón por la que se puede continuar la ejecución
  del programa sin presentar más errores.

- <***all.scm***> Contiene todos los programas en uno.

## EvalVisitor: TreeEvaluator.py
El corazón de este proyecto se encuentra en el archivo `TreeEvaluator.py`, el cual nos permite evaluar las expresiones
de los programas `.scm` previamente tokenizadas y parseados por antlr. Este código define una instancia de *visitor* bajo la clase `EvalVisitor`.
La arquitectura básica de esta se compone de las siguientes partes:
### Atributos de la clase
  - `default_labels`: Define a las operaciones y etiquetas fundamentales del lenguaje, permitiendo la operatividad básica del programa.
  - `func_lists`: Diccionario con las operaciones básicas que podemos encontrar en listas
  - `var_runtime`: Estructura de datos para almacenar y controlar las variables que se irán definiendo en tiempo de ejecución. Esta contiene dos campos por "nombre" de variable. La razón proviene de haber
    tratado de implementar dos tipos de evaluaciones diferentes según el scope en el que nos encontremos. En el caso de ser `define,` quien define a una variable, su contenido no será evaluado hasta que dicha variable sea llamada.
    Con la intención de que esta variable no se evalúe una y otra vez, presenta un campo *visited* para identificar si es necesario o no reevaluarla.  En el caso de `let`, nos encontramos con que la variable se evalúa directamente.
    Esto nos permite mostrar cómo podemos jugar con retrasar o no la evaluación de las variables definidas. La decisión de haberlo hecho con este criterio fue que, si decides crear una serie de variables con let para una determinada región
    del código, es más probable, aunque no necesario, que esta vaya a ser evaluada en algún momento de este contexto.
  - `func_runtime`: Estructura de datos para almacenar las funciones definidas en tiempo de ejecución. Entiéndase `func_runtime` como el _marco_ de una función definida.
    Cada vez que una función previamente definida sea llamada, creará una estructura que copie el contenido del _marco_ de esta función guardada. De esta manera, `func_runtime` solo funcionará
    como un contenedor de _moldes_ de funciones que permitirá dar una funcionalidad, la cual únicamente evaluará su cuerpo cuando esta sea llamada.
  - `stack_runtime`: Estructura de datos que nos permite simular el funcionamiento de una `stack`.
  - `operator_handlers`: Estructura de datos para una mayor modularidad en el código. Esta implementación fue desarrollada tras haber implementado una versión previa por evaluación con condicionales de cada expresión
    de entrada `( func *params )`.
    Debido a que estas expresiones son evaluadas por la función `visitExpr_S` del visitador, (la cual supone la mayoría del código, ya que se encarga de manejar las diferentes posibilidades de la evaluación
      basándonos en el `operator = func` que recibe de entrada) se decidió hacer un reajuste en la arquitectura de esta función, fragmentándola en diferentes `handlers` según el operador de entrada.
      ```python
      self.operator_handlers = {
                  **{op: self.handle_default_labels for op in self.default_labels},
                  **{op: self.handle_func_lists for op in self.func_lists},
                  "define": self.handle_define,
                  "read": self.handle_read,
                  "let": self.handle_let,
                  "if": self.handle_if,
                  "cond": self.handle_cond,
              }
      ```
      - `handle_default_labels`: Debido a que las funcionalidades de las etiquetas del lenguaje se han presentado en un formato breve y sencillo, pueden manejarse utilizando la misma función.
      - `handle_func_lists`: Función que permite acomodarse a las necesidades de las funciones aplicadas a listas utilizando el contenedor de funciones `func_lists`.
      - `handle_define`: Módulo para la definición de funciones y variables por el operador `define`. En el caso de definir una función, crearemos (o redefiniremos) una entrada en `func_runtime`,
        donde encontraremos: _params_, que identificará los nombres de los parámetros de la función; _body_, referenciando al cuerpo por evaluar de la función al ser llamada; y _env_, correspondiendo al entorno de la función,
        permitiendo relacionar los parámetros de la función con los dados en la función.
      - `handle_read`: Módulo para la operabilidad de la lectura de entrada estándar. Utilizamos la función _eval_ de python, la cual nos dará una excepción si nos encontramos con un string. En ese caso, evaluamos si corresponde a alguna
        de las etiquetas `#f` y `#t` para poder introducir valores bool por terminal. En el caso en el que no, será evaluado como un string.
      - `handle_let`: Permite manejar las características de un `local scope` para variables, guardando el entorno previo antes de proveer a este de las nuevas variables, para después poder 
        devolverlo como si estas variables nunca hubieran estado.
      - `handle_if`: Módulo que permite el comportamiento de lo que `John McCarthy` denominaría de `true conditional expression`, donde las instrucciones bifurcadas serán evaluadas únicamente 
        si la condición deriva a su favor.
      - `handle_cond`: Función que evalúa el caso donde el operador de entrada sea `cond`, la cual irá evaluando condiciones hasta que una se satisfaga, y por ello, se evalúe el cuerpo anexo a esta.
      - `handle_function_var_call`: Esta última funcionalidad será visitada en el caso en el que no se haya encontrado otro `handler` para el operador en cuestión. 
         Por ello, visitamos al operator, el cual nos devolverá (en el caso de existir) el contexto de la función correspondiente a este operador.

### Funciones del Visitor
Estas funciones son las generadas por las etiquetas `# ...` dadas en la gramática. Podemos encontrar:
  - ***visitRoot***: Encargada de visitar todas las expresiones desde la raíz. En la implementación de esta, se ha permitido la posibilidad de mostrar por pantalla el último resultado 
    evaluado, siempre y cuando este devuelva un resultado. De esta forma, en el caso de no tener una función main, se permita mostrar por pantalla la última operación a realizar siempre y cuando esta tenga
    un valor de retorno.
  - ***visitExpr_S***: Definida previamente por los diferentes `handlers`.
  - ***visitListElements***: Visitador para `quoted-lists`, donde, dado un patrón de listas del tipo `'( ... )`, se construye una lista.
  - ***visitNumber***: Utilizamos la función `eval()` de python, que definirá si el número es entero o `float`. Además, los valores negativos también serán correctamente evaluados debido a que se tienen presente en la gramática
  - ***visitBoolean***: Utilizando el diccionario de `default_labels`, designamos el valor de las etiquetas `#f`y `#t`. 
  - ***visitString***: Nos permite recibir un string definido por `"`.
  - *visitVar*: Este visitador gestiona las variables y funciones generadas en tiempo de ejecución, permitiendo acceder al enlace dinámico generado en la `stack`, además de comprobar si la función o variable están dentro 
    de los registros de definición de las mismas. Además, debido a que este visitador únicamente será llamado cuando no se encuentre la etiqueta del `operator`, en el caso de no estar en ninguno de los lugares previamente mencionados
    lanzaremos una excepción.

### Funciones Auxiliares
Podemos encontrar un conjunto de funciones implementadas externas a la clase que se utilizan en diversas partes de `EvalVisitor`. Debido a que la extensión de este proyecto no es demasiado grande, se ha decidido mantenerlas en el mismo archivo.
Entre ellas, podemos encontrar una función `correctOutputExpression` para mostrar en pantalla correctamente el output esperado, y cuatro funciones para el manejo de errores.
      
### EvalProgram
Esta última función será la utilizada por `scheme.py` para generar el lexer y el parser, y realizar la visita del árbol de la gramática generado, tanto para evaluarlo, como para mostrarlo en el caso de indicar `show_visit_tree=1`.

## ShowVisitor: TreeShow.py
Podemos encontrar otro `visitor` en el archivo `TreeShow.py`, como se ha comentado previamente. Con este, podemos ver el árbol generado por la expresión del programa.

## Conclusiones y Consideraciones
Creo que el propósito de este proyecto ha sido abordado, además de haber implementado algunos añadidos que me han permitido jugar con ciertos aspectos como los tiempos de evaluación, lo que considero 
ciertamente importante debido a que permite un mayor rendimiento en el programa al abstenerse de la evaluación temprana de todo el contenido del programa. Además, este proyecto me ha permitido tener una visión más profunda
sobre el comportamiento de los compiladores, donde a su vez, me ha permitido ampliar mi campo de observación sobre ciertos aspectos relacionados con los lenguajes de programación de los que previamente no era consciente o no era capaz 
de dilucidar de la misma manera.

En lo que respecta a posibles mejorías en este proyecto, creo que mostraría un mayor potencial con la implementación de expresiones lambda. Además, la búsqueda actual del `operator` se realiza poniendo dicho texto tokenizado en minúsculas,
por lo no la hace case-sensitive. A mi parecer, esto presenta ciertas ventajas a la hora de permitir algún error de escritura, aunque, a su vez, la desventaja de no permitir crear dos funciones/variables con el mismo nombre con algún tipo de diferenciación
entre letras mayúsculas y minúsculas. Con respecto a algunos fallos que podemos caracterizar, debido a que en las operaciones utilizan en el sistema de tipos de python, nos encontramos con situaciones como la evaluación de un _string_ como `True` al hacer operaciones como `and`.
Este comportamiento podría ser mitigado con un futuro chequeo de tipos más fuerte que el de python. Como otro añadido, permitir la entrada de listas como input podría haber sido una buena idea, aunque haría falta una evaluación algo más rigurosa. Para finalizar, comentar que las pruebas 
se han realizado principalmente con el evaluador, tanto manual como automáticamente. Con respecto a mostrar el recorrido del árbol, debido a que es otro añadido, no se le ha prestado la misma importancia, aunque se han realizado algunos testeos manuales de este. Podría ser interesante,
como continuación de este proyecto, el utilizarlo para mostrarlo en un formato mucho más legible, o incluso para distribuir algún tipo de check de la sintaxis. Sin embargo, para este punto del proyecto, no es necesario.


##### García Fernández, Helios
