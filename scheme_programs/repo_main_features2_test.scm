;;;=====repo_main_features2_test.scm=====
;;; Test to show more complex syntax features of Scheme in a unified repository.

;;; In this case, we divide the test into different modules unified in a main function call.

;; ============================================================
;; MODULE 4: Recursion
;; Greatest Common Factor by recursion
(define (mcd a b)
  (if (= b 0)
    a
    (mcd b (mod a b))))

;; GCF given 2 numbers by input using let to provide local scope
(define (mcd-example)
  (display "Introduce two values separately: ") (newline)
  (let ((a (read))    ;input 314
         (b (read)))  ;input 17

    (display "Greatest common factor of ")
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
    (newline)
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
    (display "Squares of the list ")(display lst) (display " --> ")
    (display (map square lst))
    (newline)))

(define (map-example2)
  (define (apply-double-twice x) (apply-twice double x))
  (let ((lst '(1 2 3 4)))
    (display "Double applied twice ")(display " of ") (display lst) (display " --> ")
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
    (display "Even numbers from ") (display lst)  (display " --> ")
    (display (filter-even lst))
    (newline)))

;; ============================================================
;; MAIN FUNCTION
(define (main)

    (display (* "==" 20))(newline)
    (display "MODULE 4: Recursion") (newline)
      (display "Running MCD Example:")
      (newline)
      (mcd-example)

    (display (* "--" 20))(newline)
      (display "Sum of List Example: ")
      (newline)
      (display "Sum '")(display '(1 2 3 4 5)) (display" = ")
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

  )
;; ============================================================
;; Program Entry Point
(main)
