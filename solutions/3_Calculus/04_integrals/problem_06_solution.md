# Exercise 6. When Does a Logarithm Appear from an Integral?

## Question

Compute

$$
\int\frac{2x}{x^2+5}\,dx.
$$

Identify the denominator as a candidate for substitution, compare the numerator with its derivative, and explain the source of the logarithm in the result.

## Solution

Choose $u=x^2+5$, with $du=2x\,dx$. Then

$$
\int\frac{2x}{x^2+5}\,dx=\int\frac{du}{u}=\ln(x^2+5)+C.
$$

The logarithm appears because its derivative is $1/u$. No absolute value is needed since $x^2+5>0$ for every real $x$. Differentiating gives $2x/(x^2+5)$, verifying the result on $\mathbb R$.
