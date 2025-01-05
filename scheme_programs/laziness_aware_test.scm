;;;=====laziness_aware_test.scm=====
;;; This test provides some examples to demonstrate laziness features in this interpreter.
(define (main)
  ;; ============================================================
  ;; MODULE 8: Difference between `let` and `define` in terms of variable evaluation using MODULE 3: I/O
  (display (* "==" 20))(newline)
  (display " MODULE 8: Difference between `let` and `define` in terms of variable evaluation using MODULE 3: I/O")(newline)

  ;; Using `let`
  ;; Echo input test to show a text read. Exception in eval returns as a string.
  (newline)
  (display "Let: Asking for an input and evaluating `read` immediately.")(newline)
  (let ((input (read)) )      ; This is your input
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
  (newline)(newline)
  ;; ============================================================
  )
(main)