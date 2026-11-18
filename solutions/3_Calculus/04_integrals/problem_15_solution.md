# Exercise 15. Recovering a Function from Its Derivative and a Condition

## Question

The function $F$ satisfies

$$
F'(x)=2xe^{x^2}
$$

and

$$
F(0)=3.
$$

1. Recognize the method needed to find the function $F$.
2. Determine the entire family of functions with the given derivative.
3. Use the condition $F(0)=3$ to determine the correct constant.
4. Verify the final result by differentiation and substitution of $x=0$.

## Solution

The factor $2x$ is the derivative of the exponent $x^2$, suggesting the substitution $u=x^2$, $du=2x\,dx$. The full family on $\mathbb R$ is

$$
F(x)=e^{x^2}+C.
$$

The condition $F(0)=3$ gives $1+C=3$, hence $C=2$ and

$$
F(x)=e^{x^2}+2.
$$

Differentiating gives $F\prime(x)=2xe^{x^2}$ and substitution gives $F(0)=1+2=3$, verifying both requirements.
