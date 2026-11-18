# Exercise 13. An Integral Depending on the Upper Limit

## Question

Let

$$
F(x)=\int_0^x(t^2+1)\,dt.
$$

Determine $F(x)$, compute $F'(x)$, and compare the result with the integrand. Explain in your own words why the height of the function describes the local rate of increase of the accumulated area.

## Solution

$$
F(x)=\left[\frac{t^3}{3}+t\right]_0^x=\frac{x^3}{3}+x,\qquad F\prime(x)=x^2+1.
$$

The derivative equals the integrand evaluated at the upper limit, in agreement with the fundamental theorem of calculus. For a small increment $h$, the added signed accumulation is $\int_x^{x+h}(t^2+1)\,dt\approx(x^2+1)h$. Dividing by $h$ and letting $h\to0$ gives the local rate of change. For negative $x$, the reversed integration direction still makes this formula valid.
