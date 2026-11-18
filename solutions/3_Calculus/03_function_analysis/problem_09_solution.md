# Exercise 9. An Oblique Asymptote

## Question

Analyze the asymptotes of

$$
f(x)=\frac{x^2+1}{x-1}.
$$

Perform polynomial division and explain why the remainder term vanishes for large $|x|$.

## Solution

Polynomial division gives

$$
f(x)=x+1+\frac2{x-1}.
$$

The domain excludes 1. The term $2/(x-1)$ tends to zero as $x\to\pm\infty$, so the oblique asymptote is $y=x+1$. At $x=1$, the numerator tends to 2 and the denominator changes sign; the left limit is $-\infty$ and the right limit is $+\infty$. Thus $x=1$ is the vertical asymptote. There is no horizontal asymptote because the linear part is unbounded.
