# Exercise 15. The Difference Quotient as a Check of the Derivative

## Question

Choose one function from the problem set and a point $x_0$ at which the derivative exists. Compute $f'(x_0)$ exactly, and then calculate

$$
\frac{f(x_0+h)-f(x_0)}h
$$

for $h=1$, $0.1$, and $0.01$. Compare the values with $f'(x_0)$ and explain why the difference quotient approaching a single number is consistent with the definition of the derivative, while a few computations do not replace a limit argument.

## Solution

Choose $f(x)=x^2-3x+1$ from Problem 10, at $x_0=2$. The exact derivative is $f\prime(2)=1$. Since $f(2)=-1$ and $f(2+h)=-1+h+h^2$,

$$
\frac{f(2+h)-f(2)}h=1+h\qquad(h\ne0).
$$

| $h$ | Difference quotient |
| --- | --- |
| 1 | 2 |
| 0.1 | 1.1 |
| 0.01 | 1.01 |

The values approach 1, consistent with the derivative. The exact formula gives the proof: $1+h\to1$ as $h\to0$ from either side. Three sampled positive steps alone would establish neither the full limit nor the behavior from negative steps.
