;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname flower-animation) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)
(require 2htdp/universe)

;;a flower planting program

;; Constants
;; =========
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

;; Data Definitions
;; ================

(define-struct flower (x y size))

;; Functions
;; =========

(define (main f)
  (big-bang f
    (on-tick tock)
    (to-draw render)
    (on-mouse handle-mouse)))

;; Flower -> Flower
;; ===========================
(define (tock f)
  (make-flower (flower-x f)
               (flower-y f)
               (add1 (flower-size f))))

;; Flower -> Image
;; ==================

(define (render f)
  (if (= (flower-size f) 0)
      MTS
      (place-image (rotate (remainder (flower-size f) 360) (scale (/ (flower-size f) 100) FLOWER))
                   (flower-x f)
                   (flower-y f)
                   MTS)))

;; Flower Integer Integer MouseEvent -> Flower
;; ==========================================

(define (handle-mouse f x y ke)
  (if (mouse=? ke "button-down")
      (make-flower x y 0)
      f))

           
