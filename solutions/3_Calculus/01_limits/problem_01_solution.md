# Exercise 1. Dominant Terms in a Sequence

## Question

Compute

$$
\lim_{n\to\infty}\frac{4n^2-3n+1}{2n^2+5n-7}.
$$

Explain why the highest-degree terms determine the result.

## Solution

Divide numerator and denominator by $n^2$:

$$
\frac{4-3/n+1/n^2}{2+5/n-7/n^2}\longrightarrow\frac42=2.
$$

The lower-degree terms vanish after this normalization. The denominator tends to the nonzero number 2, so the quotient law applies. The denominator at $n=1$ is zero, but omitting that initial index does not affect the limit of the sequence tail.
