;; TESTING


;;;=====repo_main_features2_test.scm=====
;;; Test to show more complex syntax features of Scheme in a unified repository.

;;; In this case, we divide the test into different modules unified in a main function call.

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


;; ============================================================
;; MAIN FUNCTION
(define (main)

  (display (* "==" 20)) (newline)
  (display "MODULE 4: Recursion") (newline)
  (display "Running MCD Example:")
  (newline)
  (mcd-example)

  )
;; ============================================================
;; Program Entry Point
(main)
