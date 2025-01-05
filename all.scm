;;;=====all.scm=====
;;;It allows to execute all the programms at once

;; ============================================================
(display (* "=" 40 ))(newline)
;; MODULE 1: Default Operators
(display "MODULE 1: Default Operators") (newline)
;; Arithmetic Operations. Use of read to set variables a=10 and b=5
(display (* "-" 40 ))(newline)
(display "Arithmetic Operations:") (newline)
(display "Value a: ") ; input 10
(define a (read)) (display a) (newline)
(display "Value b: ") ; input 5
(define b (read)) (display b) (newline)

(display "(+ a b) ")(display (+ a b)) ; Addition, Result: 15
(newline)
(display "(- a b) ")(display (- a b)) ; Subtraction, Result: 5
(newline)
(display "(* a b) ")(display (* a b)) ; Multiplication, Result: 50
(newline)
(display "(/ a b) ")(display (/ a b)) ; Division, Result: 2
(newline)
(display "(div a b) ")(display (div a b)) ; Float Division, Result: 2.0
(newline)
(display "(mod a b) ")(display (mod a b)) ; Module, Result: 0
(newline)


;; Relational Operators. Redefining a=5 and b=3
(display (* "-" 40 ))(newline)
(display "Relational Operators:") (newline)
(display "Value a: ") ; input 5
(define a (read)) (display a) (newline)
(display "Value b: ") ; input 3
(define b (read)) (display b) (newline)

(display "(> a b) ")(display (> a b)) ; Result: #t 5 > 3
(newline)
(display "(< b a) ")(display (< b a)) ; Result: #t 3 < 5
(newline)
(display "(= a b) ")(display (= a b)) ; Result: #f 5 == 3
(newline)
(display "(>= b b) ")(display (>= b b)) ; Result: #t 5 >= 5
(newline)
(display "(<= a b) ")(display (<= a b)) ; Result: #f 5 <= 3
(newline)

;; Booleans. Defining variables a=#f b=5 c=3
(display (* "-" 40 ))(newline)
(display "Boolean Operators:") (newline)
(display "Value a: ") ; input #t
(define a (read)) (display a) (newline)
(display "Value b: ") ; input 5
(define b (read)) (display b) (newline)
(display "Value c: ") ; input 3
(define c (read)) (display c) (newline)

(display "(and a (< c b)) ") (display (and a (< c b)))             ; Resultat: #t
(newline)
(display "(or (> b c) (< 1 0)) ") (display (or (> b c) (< 1 0)))   ; Resultat: #t
(newline)
(display "(not a)") (display (not a) )                             ; Resultat: #f
(newline)

;; ============================================================
(display (* "=" 40 ))(newline)
;; MODULE 2: Define and Conditionals
(display "MODULE 2: Define and Conditionals") (newline)

;;; Defining Constants
(display (* "-" 40 ))(newline)
(display "Defining Constants:") (newline)
(define pi 3.14159)
(define radius 5)
(display "Circle Area with radius 5: ")
(display (* pi (* radius radius))) ; Circle Area, Result: 78.53975
(newline)

;;; Defining basic function
(display (* "-" 40 ))(newline)
(display "Defining Sum:") (newline)
(define (sum x y)
  (+ x y))
(display " Sum of 3 and 4 is ")
(display (sum 3 4)) ; Function sum, Result: 7
(newline)

;;; Conditional if with function define
(display (* "-" 40 ))(newline)
(display "Conditional `if`:") (newline)
(define (compare-values x y)
  (if (> x y)
      "x is greater"
      (if (< x y)
          "y is greater"
          "x and y are equal")))
(display (compare-values 5 3)) ; Result: "x is greater"
(newline)
(display (compare-values 3 5)) ; Result: "y is greater"
(newline)
(display (compare-values 3 3)) ; Result: "x and y are equal"
(newline)

;;; Multiple Conditions with cond
(display (* "-" 40 ))(newline)
(display "Multiple Conditions with cond:") (newline)

(define (number-description n)
  (cond
    ((> n 0) "Positive")
    ((< n 0) "Negative")
    (#t "Zero"))
)
(display (number-description 5)) ; Result: "Positive"
(newline)
(display (number-description -3)) ; Result: "Negative"
(newline)
(display (number-description 0)) ; Result: "Zero"
(newline)

(display "Redifining number-description using cond with else:") (newline)
(define (number-description n)
  (cond
    ((> n 0) "Positive")
    ((< n 0) "Negative")
    (else "Zero"))
)
(display (number-description 5)) ; Result: "Positive"
(newline)
(display (number-description -3)) ; Result: "Negative"
(newline)
(display (number-description 0)) ; Result: "Zero"
(newline)

;; ============================================================
(display (* "=" 40 ))(newline)
;; MODULE 3: Lists
(display "MODULE 3: Lists") (newline)

;;; Lists
(display (* "-" 40 ))(newline)
(display "List operators ") (newline)

(define my-list '(1 2 3 4 5))
(display "my-list = ") (display my-list)(newline)
(display "(car my-list): ")(display (car my-list))        ; Result: 1
(newline)
(display "(cdr my-list): ")(display (cdr my-list))        ; Result: (2 3 4 5)
(newline)
(display "(cons 0 my-list): ")(display (cons 0 my-list))  ; Result: (0 1 2 3 4 5)
(newline)
(display "(null? '()): ")(display (null? '()))            ; Result: #t
(newline)
(display "(null? my-list): ")(display (null? my-list))    ; Result: #f
(newline)

(display (* "-" 40 ))(newline)
(display "Lists are not mutable. List provided: ")
(define my-list (cons 0 (cons 1 (cons 2 (cons 3 '())))))
(display my-list)
(newline)
(display "List provided after cons 1: ")
(define lst-cons my-list)           ;new variable that save the list
(define lst-cons (cons 1 lst-cons)) ;alterate the new variable
(display my-list)                   ; Result: (0 1 2 3)
(newline)


;; ============================================================
;; MODULE 4: Recursion
;; Greatest Common Divisor by recursion
(define (mcd a b)
  (if (= b 0)
    a
    (mcd b (mod a b))))

;; GCD given 2 numbers by input using let to provide local scope
(define (mcd-example)
  (display "Introduce two values separately: ") (newline)
  (let ((a (read))    ;input 314
         (b (read)))  ;input 17

    (display "Greater common divisor of ")
    (display a) (display " and ") (display b) (display " is: ")
    (display (mcd a b))
    (newline)
    )
  )

;; To sum all elements of a list using recursion
(define (suma-llista llista)
  (if (null? llista)
    0
    (+ (car llista) (suma-llista (cdr llista)))))

;; Final Recursive factorial function


(define (factorial-tail n)
  (define (inner-fact n acc)
    (if (= n 0)
        acc
        (inner-fact (- n 1) (* n acc))))
  (inner-fact n 1))

(define (factorial-example)
    (define n (read))(display n)
    (display "! is ")
    (display (factorial-tail n))
    (newline))

;; ============================================================
;; MODULE 5: Local Variables and Scoping
;; Use of `let` for local scope and nested scoping
(define (let-example)
  (let ((x (read)) ; input 5
         (y (read)))   ; input 10
    (let ((z (+ x y)))
      (display "Sum of ") (display x) (display " and ") (display y) (display " is: ")
      (display z)
      (newline))))

;; ============================================================
;; MODULE 6: I/O
;; Echo input test to show a text readed. Exception in eval, return as a str
(define (echo-input)
  (display "Enter a sentence: ")
  (let ((input (read)))
    (display "You entered: ")
    (display input)
    (newline)))

;; ============================================================
;; MODULE 7: Higher-Order Functions
;; Doubles a number
(define (double x)
  (* x 2))

;; Applies a function twice
(define (apply-twice f x)
  (f (f x)))

;; Example of applying a function twice
(define (twice-example)
  (let ((x 5))
    (display "Twice of double of ")
    (display x)
    (display " is ")
    (display (apply-twice double x))
    (newline)))

;; Example using map
(define (map func lst)
  (cond
    ((null? lst) '())
    (else (cons (func (car lst)) (map func (cdr lst))))))

(define (map-example1)
  (define (square x) (* x x))
  (let ((lst '(1 2 3 4)))
    (display "Squares of the list: ")
    (display (map square lst))
    (newline)))

(define (map-example2)
  (define (apply-double-twice x) (apply-twice double x))
  (let ((lst '(1 2 3 4)))
    (display "Double applied twice: ")
    (display (map apply-double-twice lst))
    (newline)))

;; Filters even numbers from a list
(define (filter predicate lst)
  (cond
    ((null? lst) '())  ;
    ((predicate (car lst))
      (cons (car lst) (filter predicate (cdr lst))))
    (#t (filter predicate (cdr lst)))))

(define (filter-even lst)
  (define (even? x) (= (mod x 2) 0))
  (filter even? lst))

(define (filter-example)
  (let ((lst '(1 2 3 4 5 6)))
    (display "Even numbers from the list: ")
    (display (filter-even lst))
    (newline)))



(define (error-checker-examples)

  (display (* "==" 20))(newline)
  (display "MODULE 10: Error Checkers") (newline)
  (display
"Most of the necessary error handlers occur because of the logic implemented in python.
  To highlight some of them, I wanted to add the following.
  Those that do not cause a direct effect on the program logic
   are the ones that would really be necessary to implement,
  which are those that have been detected and have not been commented out.")
  (newline)(display (* "--" 20))(newline)
  ;;Error in `define`: Too many arguments to define a variable
  (display "Too many arguments in `define` (variable) :")
  (newline)(define v1 (read))(define v2 (read))
  (display "(define var v1 v2) -> ")(define var v1 v2)
  (newline)
  (display (* "--" 20))(newline)

#|***
  ;; Error in `define`: Missing body
  (display "Missing body in `define`:")
  (newline)
  (define (nobody-func) )
  (newline)
  (display (* "--" 20))(newline)
|#

#|***
  ;; Error in `read`: Arguments provided when none are expected
  (display "`read` with arguments:")
  (newline)
  (display "(read '()) -> ")(read '())
  (newline)
  (display (* "--" 20))(newline)
|#

#|***
  ;; Error in `let`: Unexpected number of arguments
  (display "Error1: `let` defining variables: Too Many arguments")
  (newline)
  (display "(let ((x 3 2)) -> ")(let ((x 3 2)) )
  (newline)
  (display (* "--" 20))(newline)
|#
#|***
  (display "Error2: `let` defining variables: Not enough arguments")
  (newline)
  (display "(let ((x )) -> ")(let ((x )) )
  (newline)
  (display (* "--" 20))(newline)
|#

    (newline)
  ;; Error in `if`: Invalid number of arguments
  (display "Error: `if` with invalid number of arguments:")
  (newline)
  (display "(if C, N1, N2, N3) -> ") (if #t 1 2 3)
  (newline)


#|***
  (display "(if C ) -> " )(if #t ())
  (newline)
|#
  (display (* "--" 20))(newline)

#|***
  ;; Undefined function or variable
  (display "Error: Undefined function or variable:")
  (newline)
  (display "Calling (undefined-function 1 2 3) -> ") (display (undefined-function 1 2 3))
  (newline)
|#
  (display (* "--" 20))(newline)
  (display "***There are more examples than the ones that are printed.
  Because they will directly affect the logic of the interpreter,
  they are commented out. They will raise their error handler implemented
  if `raiseError` undo comment at `raise`.***")
(newline)
)
;; ============================================================
;; MAIN FUNCTION
(define (main)

    (display (* "==" 20))(newline)
    (display "MODULE 4: Recursion") (newline)
      (display "Running MCD Example:")
      (newline)
      (mcd-example)

    (display (* "--" 20))(newline)
      (display "Sum of List Example:")
      (newline)
      (display (suma-llista '(1 2 3 4 5))) ; Result: 15
      (newline)
      (display (* "--" 20))(newline)

      (display "Factorial-Tail-Recursive Example:")
      (newline)
      (factorial-example)           ; Result: 2432902008176640000


    (display (* "==" 20))(newline)
    (display "MODULE 5: Local Variables and Scoping")(newline)
      (display "Let Scope Example:")
      (newline)
      (let-example)

    (display (* "==" 20))(newline)
    (display "MODULE 6: I/O")(newline)
      (display "Echo Input Example")
      (newline)
      (echo-input)

  (display (* "==" 20)) (newline)
  (display "MODULE 7: Higher-Order Functions") (newline)

  (display "Twice Example ")
  (newline)
  (twice-example)
  (display (* "--" 20)) (newline)
  (display "Map Example 1")
  (newline)
  (map-example1)    ; Result: (1 4 9 16)
  (newline)
  (display "Map Example 2")
  (newline)
  (map-example2)    ; Result: (4 8 12 16)

  (display (* "--" 20)) (newline)
  (display "Filter Example ")
  (newline)
  (filter-example)
  (display (* "==" 20)) (newline)


;; ============================================================
;; MODULE 8: Difference between `let` and `define` in terms of variable evaluation using MODULE 3: I/O
(display (* "==" 20))(newline)
(display " MODULE 8: Difference between `let` and `define` in terms of variable evaluation using MODULE 3: I/O")(newline)

;; Using `let`
;; Echo input test to show a text read. Exception in eval returns as a string.

(display "Let: Asking for an input and evaluating `read` immediately.")
(let ((input (read)))      ; This is your input
  (display "This is your input: ")
  (display input)
  (newline))

;; Using `define`
(display "Define: Asking for an input and evaluating `read` only when the variable `input` is accessed.")
(define input (read))
(display "You have not accessed your input yet, but the variable `input` is declared.")
(newline)
(display "Now we access your input and display it:")
(display input) (newline)
(display "Input displayed")
(newline)
;; ============================================================

  ;; ============================================================
;; MODULE 9: DEFINE and LET Scopes
(display (* "==" 20))(newline)
(display " MODULE 9: DEFINE and LET Scopes")(newline)

;; Using DEFINE
(display "Define affects the global scope")(newline)

(define x1 (read))
(define x2 (read))

(define (define-vars)
  (define x1 (read))  ; Redefine x1 locally
  (define x2 (read))  ; Redefine x2 locally
  (display "Inside DEFINE function scope:")(newline)
  (display "Var x1: ")(display x1)(newline)
  (display "Var x2: ")(display x2)(newline))

(display "Before calling DEFINE function:")(newline)
(display "Var x1: ")(display x1)(newline)
(display "Var x2: ")(display x2)(newline)

(define-vars)

(display "After calling DEFINE function:")(newline)
(display "Var x1: ")(display x1)(newline)
(display "Var x2: ")(display x2)(newline)

;; Using LET
(display "Let creates a new scope and does not affect the global scope")(newline)

(display "Before entering LET scope:")(newline)
(display "Var x1: ")(display x1)(newline)
(display "Var x2: ")(display x2)(newline)

(let ((x1 (read)) (x2 (read)) (x3 (read)))
  (display "Inside the LET scope:")(newline)
  (display "Var x1: ")(display x1)(newline)
  (display "Var x2: ")(display x2)(newline)
  (display "Var x3: ") (display x3)(newline))

(display "After exiting LET scope:")(newline)
(display "Var x1: ")(display x1)(newline)
(display "Var x2: ")(display x2)(newline)
(display "Var x3 will raise an error because it is not defined in the global scope") (newline)
(display "Var x3: ")(display x3)(newline) ;;raise an error.
;; ============================================================

;; ============================================================
;; MODULE 10: Error Checkers
;; Demonstrates error handling for various syntax and runtime issues.


;; ============================================================
(error-checker-examples)


  )
;; ============================================================
;; Program Entry Point

(main)



