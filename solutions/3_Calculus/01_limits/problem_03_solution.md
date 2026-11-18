# Exercise 3. A Square Root and Removing an Indeterminate Form

## Question

Compute

$$
\lim_{n\to\infty}\left(\sqrt{n^2+5n}-n\right).
$$

Use the conjugate expression and explain why this transformation removes the difficulty.

## Solution

Multiply by the conjugate to replace subtraction of large nearly equal quantities with a quotient:

$$
\sqrt{n^2+5n}-n=\frac{5n}{\sqrt{n^2+5n}+n}=\frac5{\sqrt{1+5/n}+1}\longrightarrow\frac52.
$$

This resolves the indeterminate form $\infty-\infty$ and leaves a denominator tending to 2.
