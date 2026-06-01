(defun trapezoidal-rule (f a b n)
  "Calculates the area under curve 'f' from 'a' to 'b' using 'n' intervals."
  (let* ((dx (/ (- b a) n))
         (initial-sum (* 0.5 (+ (funcall f a) (funcall f b)))))
    (labels ((sum-loop (i acc)
               (if (= i n)
                   acc
                   (let ((x (+ a (* i dx))))
                     (sum-loop (1+ i) (+ acc (funcall f x)))))))
      (* dx (sum-loop 1 initial-sum)))))

;; 1. Define the curve/function: f(x) = x^2
(defun my-curve (x)
  (* x x))

;; 2. Set the parameters
(let ((start-x 0.0)
      (end-x 4.0)
      (intervals 1000))

  ;; 3. Calculate and print the area
  (let ((area (trapezoidal-rule #'my-curve start-x end-x intervals)))
    (format t "The approximate area under the curve is: ~F~%" area)))
