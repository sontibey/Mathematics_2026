# Exercise 4. Substitution as Reversing the Chain Rule

## Question

Compute

$$
\int 2x(x^2+1)^4\,dx.
$$

Before calculating, identify a candidate for the new variable $u$ and show that its derivative appears in the integral. Finally, verify the result by differentiation.

## Solution

The fourth power contains the inner expression $x^2+1$. Its derivative is $2x$, exactly the other factor in the integrand. This is the chain-rule structure $g(u(x))u'(x)$, so choose

$$
u=x^2+1,\qquad du=2x\,dx.
$$

The substitution absorbs the entire factor $2x\,dx$ and leaves a power of $u$:

$$
\int 2x(x^2+1)^4\,dx=\int u^4\,du=\frac{u^5}{5}+C.
$$

Returning to the original variable gives

$$
F(x)=\frac{(x^2+1)^5}{5}+C.
$$

The division by 5 cancels the factor from differentiating the fifth power. The remaining chain-rule factor must also be checked:

$$
F'(x)=\frac15\cdot5(x^2+1)^4\cdot2x=2x(x^2+1)^4.
$$

This derivative identity is valid for every real $x$, including zero. It establishes the antiderivative globally without dividing by $x$ or requiring $x^2+1$ to be one-to-one on the whole real line.
