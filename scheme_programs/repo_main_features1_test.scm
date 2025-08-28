;;;=====repo_main_features1_test.scm=====
;;;Test to show basic syntax operations with Scheme

(define (main)
  ;; ============================================================
  (display (* "=" 40)) (newline)
  ;; MODULE 1: Default Operators
  (display "MODULE 1: Default Operators") (newline)
  ;; Arithmetic Operations. Use of read to set variables a=10 and b=5
  (display (* "-" 40)) (newline)
  (display "Arithmetic Operations:") (newline)
  (display "Value a: ") ; input 10
  (define a (read)) (display a) (newline)
  (display "Value b: ") ; input 5
  (define b (read)) (display b) (newline)

  (display "(+ a b) ") (display (+ a b)) ; Addition, Result: 15
  (newline)
  (display "(- a b) ") (display (- a b)) ; Subtraction, Result: 5
  (newline)
  (display "(* a b) ") (display (* a b)) ; Multiplication, Result: 50
  (newline)
  (display "(/ a b) ") (display (/ a b)) ; Division, Result: 2
  (newline)
  (display "(div a b) ") (display (div a b)) ; Float Division, Result: 2.0
  (newline)
  (display "(mod a b) ") (display (mod a b)) ; Module, Result: 0
  (newline)


  ;; Relational Operators. Redefining a=5 and b=3
  (display (* "-" 40)) (newline)
  (display "Relational Operators:") (newline)
  (display "Value a: ") ; input 5
  (define a (read)) (display a) (newline)
  (display "Value b: ") ; input 3
  (define b (read)) (display b) (newline)

  (display "(> a b) ") (display (> a b)) ; Result: #t 5 > 3
  (newline)
  (display "(< b a) ") (display (< b a)) ; Result: #t 3 < 5
  (newline)
  (display "(= a b) ") (display (= a b)) ; Result: #f 5 == 3
  (newline)
  (display "(>= b b) ") (display (>= b b)) ; Result: #t 5 >= 5
  (newline)
  (display "(<= a b) ") (display (<= a b)) ; Result: #f 5 <= 3
  (newline)

  ;; Booleans. Defining variables a=#f b=5 c=3
  (display (* "-" 40)) (newline)
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
  (display "(not a)") (display (not a))                             ; Resultat: #f
  (newline)

  ;; ============================================================
  (display (* "=" 40)) (newline)
  ;; MODULE 2: Define and Conditionals
  (display "MODULE 2: Define and Conditionals") (newline)

  ;;; Defining Constants
  (display (* "-" 40)) (newline)
  (display "Defining Constants:") (newline)
  (define pi 3.14159)
  (define radius (read))
  (display "Circle Area with radius ") (display radius) (display " is ")
  (display (* pi (* radius radius))) ; Circle Area, Result: 78.53
  (newline)

  ;;; Defining basic function
  (display (* "-" 40)) (newline)
  (display "Defining Sum:") (newline)
  (define s1 (read)) (define s2 (read))
  (define (sum x y)
    (+ x y))
  (display " Sum of ") (display s1) (display " and ") (display s2) (display " is ")
  (display (sum s1 s2)) ; Function sum, Result: 7
  (newline)

  ;;; Conditional if with function define
  (display (* "-" 40)) (newline)
  (define i1 (read)) (define i2 (read))
  (display "Conditional `if`:") (newline)
  (define (compare-values x y)
    (if (> x y)
      "x is greater"
      (if (< x y)
        "y is greater"
        "x and y are equal")))
  (display "x=") (display i1)(display " and ") (display "y=") (display i2) (display " -> ")
  (display (compare-values i1 i2)) ; Result: "x is greater"
  (newline)
  (display "x=") (display i2)(display " and ") (display "y=") (display i1) (display " -> ")
  (display (compare-values i2 i1)) ; Result: "y is greater"
  (newline)
  (display "x=") (display i1)(display " and ") (display "y=") (display i1) (display " -> ")
  (display (compare-values i1 i1)) ; Result: "x and y are equal"
  (newline)

  ;;; Multiple Conditions with cond
  (display (* "-" 40)) (newline)
  (display "Multiple Conditions with cond:") (newline)

  (define (number-description n)
    (cond
      ((> n 0) "Positive")
      ((< n 0) "Negative")
      (#t "Zero"))
    )
  (define c1 (read)) (define c2 (read)) (define c3 (read))
  (display c1) (display " is ")
  (display (number-description c1)) ; Result: "Positive"
  (newline)
  (display c2) (display " is ")
  (display (number-description c2)) ; Result: "Negative"
  (newline)
  (display c3) (display " is ")
  (display (number-description c3)) ; Result: "Zero"
  (newline)
  (display "Redifining number-description using cond with else:") (newline)
  (define (number-description n)
    (cond
      ((> n 0) "Positive")
      ((< n 0) "Negative")
      (else "Zero"))
    )
  (display c1) (display " is ")
  (display (number-description c1)) ; Result: "Positive"
  (newline)
  (display c2) (display " is ")
  (display (number-description c2)) ; Result: "Negative"
  (newline)
  (display c3) (display " is ")
  (display (number-description c3)) ; Result: "Zero"
  (newline)

  ;; ============================================================
  (display (* "=" 40)) (newline)
  ;; MODULE 3: Lists
  (display "MODULE 3: Lists") (newline)

  ;;; Lists
  (display (* "-" 40)) (newline)
  (display "List operators ") (newline)

  (define my-list '(1 2 3 4 5))
  (display "my-list = ") (display my-list) (newline)
  (display "(car my-list): ") (display (car my-list))        ; Result: 1
  (newline)
  (display "(cdr my-list): ") (display (cdr my-list))        ; Result: (2 3 4 5)
  (newline)
  (display "(cons 0 my-list): ") (display (cons 0 my-list))  ; Result: (0 1 2 3 4 5)
  (newline)
  (display "(null? '()): ") (display (null? '()))            ; Result: #t
  (newline)
  (display "(null? my-list): ") (display (null? my-list))    ; Result: #f
  (newline)

  (display (* "-" 40)) (newline)
  (display "Lists are not mutable. List provided: ")
  (define my-list (cons 0 (cons 1 (cons 2 (cons 3 '())))))
  (display my-list)
  (newline)
  (display "List provided after cons 1: ")
  (define lst-cons my-list)           ;new variable that save the list
  (define lst-cons (cons 1 lst-cons)) ;alterate the new variable
  (display my-list)                   ; Result: (0 1 2 3)
  (newline)
  )
  ;; ============================================================
;; Program Entry Point
(main)



