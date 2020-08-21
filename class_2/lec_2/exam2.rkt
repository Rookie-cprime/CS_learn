;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname exam2) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
 ;write the signature
;;Number -> Number
;write the purpose
;;produce 2 times the given number
;stub
;(define (double n) 0);this is stub

;exampels/tests
(check-expect (double 3) 6)
(check-expect (double 4.2) 8.4)

;template/inventory
;(define (double n)
;  (... n))

;code body
(define (double n)
  (* 2 n))
