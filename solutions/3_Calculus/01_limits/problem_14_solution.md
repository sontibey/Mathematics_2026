# Exercise 14. A $0/0$ Limit with Trigonometry

## Question

Compute

$$
\lim_{x\to0}\frac{1-\cos x}{x^2}.
$$

Justify the result without using l'Hôpital's rule, using a trigonometric identity and the fundamental limit.

## Solution

Use $1-\cos x=2\sin^2(x/2)$:

$$
\frac{1-\cos x}{x^2}=\frac12\left(\frac{\sin(x/2)}{x/2}\right)^2\longrightarrow\frac12.
$$

This uses only the angle-halving identity and the fundamental sine limit, without l’Hôpital’s rule.
