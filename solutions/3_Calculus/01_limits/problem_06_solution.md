# Exercise 6. From a Sequence to a Function — Limit at Infinity

## Question

Compute

$$
\lim_{x\to\infty}\frac{3x^2-x+1}{5x^2+4x-2}.
$$

Compare the method with Exercise 1. Explain what changes when moving from $n$ to a real variable $x$, and what stays the same.

## Solution

$$
\frac{3x^2-x+1}{5x^2+4x-2}=\frac{3-1/x+1/x^2}{5+4/x-2/x^2}\longrightarrow\frac35.
$$

As in Exercise 1, divide by the highest power and use the quotient law. The difference is that $x$ can approach infinity through any real values in the domain, not just integers; the same bounds on $1/x$ and $1/x^2$ apply.
