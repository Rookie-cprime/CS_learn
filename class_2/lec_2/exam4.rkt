;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname exam4) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;; Number -> Number
;; given length of one side of square,produce the area of the square
(check-expect (area 3) 9)
(check-expect (area 3.2) (* 3.2 3.2))

;(define (area a) 0);stub

;(define (area s)
;  (... s))

(define (area s)
  (* s s))