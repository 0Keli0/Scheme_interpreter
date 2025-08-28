;;;=====scope_test.scm=====
;;; This test demonstrates the difference in scoping between `define` and `let`.

(define (main)
  ;; ============================================================
  ;; MODULE 9: DEFINE and LET Scopes
  (display (* "==" 20)) (newline)
  (display " MODULE 9: DEFINE and LET Scopes") (newline)

  ;; Using DEFINE
  (display "Define affects the global scope") (newline)

  (define x1 (read))
  (define x2 (read))

  (define (define-vars)
    (define x1 (read))  ; Redefine x1 locally
    (define x2 (read))  ; Redefine x2 locally
    (display "Inside DEFINE function scope:") (newline)
    (display "Var x1: ") (display x1) (newline)
    (display "Var x2: ") (display x2) (newline))

  (display "Before calling DEFINE function:") (newline)
  (display "Var x1: ") (display x1) (newline)
  (display "Var x2: ") (display x2) (newline)

  (define-vars)

  (display "After calling DEFINE function:") (newline)
  (display "Var x1: ") (display x1) (newline)
  (display "Var x2: ") (display x2) (newline)

  ;; Using LET
  (display "Let creates a new scope and does not affect the global scope") (newline)

  (display "Before entering LET scope:") (newline)
  (display "Var x1: ") (display x1) (newline)
  (display "Var x2: ") (display x2) (newline)

  (let ((x1 (read)) (x2 (read)) (x3 (read)))
    (display "Inside the LET scope:") (newline)
    (display "Var x1: ") (display x1) (newline)
    (display "Var x2: ") (display x2) (newline)
    (display "Var x3: ") (display x3) (newline))

  (display "After exiting LET scope:") (newline)
  (display "Var x1: ") (display x1) (newline)
  (display "Var x2: ") (display x2) (newline)
  (display "Var x3 will raise an error because it is not defined in the global scope") (newline)
  (display "Var x3: ") (display x3) (newline) ;;raise an error.

  )
  ;; ============================================================
;; Program Entry Point
(main)

