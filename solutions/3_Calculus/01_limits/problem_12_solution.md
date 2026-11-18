# Exercise 12. Exponential Function Limit

## Question

Compute

$$
\lim_{x\to0}(1+3x)^{1/x}.
$$

Connect the result with the limit from Exercise 5 and show the appropriate transformation.

## Solution

The base is positive for $x$ sufficiently close to zero. Put $u=3x$:

$$
(1+3x)^{1/x}=\left((1+u)^{1/u}\right)^3\longrightarrow e^3.
$$

The real-variable fundamental limit follows from $\ln(1+u)/u\to1$ as $u\to0$, on both sides within $u>-1$. This is the same logarithmic pattern as Exercise 5, with the exponent producing the additional factor 3.
