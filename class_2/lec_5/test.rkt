;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname test) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)
(require 2htdp/universe)

(define WIDTH 400)
(define HEIGHT 600)
(define MTS (empty-scene WIDTH HEIGHT "green"))

(define CENTER (circle 15 "solid" "yellow"))
(define PETAL (ellipse 30 50 "solid" "purple"))
(define FLOWER
  (overlay (above CENTER (rectangle 1 10 0 "white"))
           (overlay/align "center" "top" (above (beside (rotate 216 PETAL) (rectangle 1 1 0 "white") (rotate 144 PETAL))
                                                (rotate 180 (beside (rotate 72 PETAL) (rectangle 10 0 0 "white") (rotate 288 PETAL))))
                          (above (rectangle 1 61 0 "white") PETAL))))
(scale (/ 200 100) FLOWER)