;;;=====error_checkers_test.scm=====
;;; Test to show syntax features and error checkers of Scheme in a unified repository.

;;; This case includes various modules, with an additional one focusing on error demonstration.

;; ============================================================
;; MODULE 10: Error Checkers
;; Demonstrates error handling for various syntax and runtime issues.

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
(error-checker-examples)

