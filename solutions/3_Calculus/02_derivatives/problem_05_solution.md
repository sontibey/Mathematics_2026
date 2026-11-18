# Exercise 5. The Chain Rule as Working Through Layers

## Question

For

$$
f(x)=(3x^2-2x+1)^5
$$

identify the inner and outer functions, compute their derivatives, and combine the result according to the chain rule. Explain the origin of the additional factor.

## Solution

Take the inner function $u(x)=3x^2-2x+1$ and outer function $g(u)=u^5$. Their derivatives are $u\prime(x)=6x-2$ and $g\prime(u)=5u^4$. Thus

$$
f\prime(x)=5(3x^2-2x+1)^4(6x-2).
$$

The extra factor $6x-2$ accounts for the rate at which the inner input changes with $x$. All functions here are defined and differentiable on the real line.
