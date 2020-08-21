;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname letter-grade-starter) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;; LetterGrade is one of:
;; - "A"       
;; - "B"       
;; - "C"       
;; interp. the letter grade in a course

;;<examples are redundant for enmuerations>
(define (fn-for-letter-grade lg)
  (cond [(string=? lg "A") (... lg)]
        [(string=? lg "B") (... lg)]
        [(string=? lg "C") (... lg)])
  )

;;Template rules use:
;;- one of: