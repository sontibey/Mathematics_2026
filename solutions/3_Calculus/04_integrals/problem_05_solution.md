# Exercise 5. The Same Substitution in a Different Context

## Question

Compute

$$
\int xe^{x^2}\,dx.
$$

First compare the structure with Problem 4 and explain what is common despite the different appearance of the function.

## Solution

In Problem 4, the integral has the form $g(u(x))u'(x)$ with $u=x^2+1$. Here the outer function is an exponential and the inner expression is $x^2$. The structural question remains the same: is the derivative of the inner expression present as a factor?

For $u=x^2$, the derivative is $2x$, while the integrand contains only $x$. Therefore a factor of $1/2$ is needed:

$$
u=x^2,\qquad du=2x\,dx,\qquad x\,dx=\frac12\,du.
$$

The resulting calculation is

$$
\int xe^{x^2}\,dx=\frac12\int e^u\,du
=\frac12e^u+C=\frac12e^{x^2}+C.
$$

An antiderivative of $e^u$ is $e^u$ itself. The coefficient is essential: without the half, differentiation would give twice the required integrand. Explicitly,

$$
\frac{d}{dx}\left(\frac12e^{x^2}+C\right)
=\frac12e^{x^2}\cdot2x=xe^{x^2}.
$$

This holds on all of $\mathbb R$. The two exercises use different outer functions, but both work by recognizing an inner derivative rather than expanding the integrand.
