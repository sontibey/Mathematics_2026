# Exercise 12. Several Rules at Once

## Question

For

$$
f(x)=(x^2+1)^3e^x
$$

compute the derivative. Before calculating, write down a plan: which rule applies to the whole expression and which rule applies to one of its factors. Finally, organize the result by factoring out common factors.

## Solution

Use the product rule on the whole expression, and the chain rule on $(x^2+1)^3$.

$$
f\prime(x)=6x(x^2+1)^2e^x+(x^2+1)^3e^x=(x^2+1)^2e^x(x^2+6x+1).
$$

The factor $6x$ combines the outer power derivative 3 with the inner derivative $2x$. Factoring preserves both product-rule contributions.
