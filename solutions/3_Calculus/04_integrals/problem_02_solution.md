# Exercise 2. Powers, Roots, and the Domain

## Question

Compute

$$
\int\left(2\sqrt{x}+\frac{3}{x^2}-x^{1/3}\right)\,dx.
$$

First rewrite the terms as powers, determine the domain of the original expression, and verify the result by differentiation.

## Solution

The original expression includes both a square root and a reciprocal. The square root restricts the real input to $x\ge0$, while the reciprocal excludes zero. Therefore the domain is the single interval $(0,\infty)$.

On this interval, rewrite the integrand as

$$
2x^{1/2}+3x^{-2}-x^{1/3}.
$$

For a power $x^p$ with $p\ne-1$, increasing the exponent by one and dividing by the new exponent reverses differentiation. None of the three exponents is $-1$, so no logarithmic term is needed. The three contributions are

$$
\frac{2}{3/2}x^{3/2}=\frac43x^{3/2},\qquad
\frac{3}{-1}x^{-1}=-\frac3x,\qquad
-\frac{1}{4/3}x^{4/3}=-\frac34x^{4/3}.
$$

Combining them gives

$$
\int\left(2\sqrt{x}+\frac3{x^2}-x^{1/3}\right)\,dx
=\frac43x^{3/2}-\frac3x-\frac34x^{4/3}+C,\qquad x>0.
$$

In particular, the positive reciprocal term integrates to a negative reciprocal, since differentiating $x^{-1}$ supplies a minus sign. Check all coefficients and exponents by differentiating:

$$
\frac{d}{dx}\left(\frac43x^{3/2}-3x^{-1}-\frac34x^{4/3}+C\right)
=\frac43\frac32x^{1/2}+3x^{-2}-\frac34\frac43x^{1/3}
=2\sqrt{x}+\frac3{x^2}-x^{1/3}.
$$

This verification holds on the original domain; the formula does not extend the original integrand to zero or negative inputs.
