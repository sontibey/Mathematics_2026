# Exercise 7. Integration by Parts as Reversing the Product Rule

## Question

Compute

$$
\int xe^x\,dx.
$$

First write the product differentiation rule and, on that basis, explain the meaning of the integration-by-parts formula. Verify the result by differentiation.

## Solution

The product rule $(uv)\prime=u\prime v+uv\prime$ rearranges, after integrating, to $\int u\,dv=uv-\int v\,du$. Choose $u=x$, $dv=e^x\,dx$, so $du=dx$, $v=e^x$.

$$
\int xe^x\,dx=xe^x-\int e^x\,dx=(x-1)e^x+C.
$$

The derivative is $e^x+(x-1)e^x=xe^x$, confirming the antiderivative.
