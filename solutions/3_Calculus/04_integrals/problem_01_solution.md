# Exercise 1. Antiderivative and Verification

## Question

For

$$
f(x)=3x^2-4x+5
$$

find one antiderivative $F(x)$. Write the entire family of antiderivatives, verify the result by differentiation, and explain the meaning of the constant $C$.

## Solution

An antiderivative must differentiate to the given polynomial. Each monomial can be treated separately because differentiation is linear. To obtain $3x^2$, choose $x^3$; to obtain $-4x$, choose $-2x^2$; to obtain the constant 5, choose $5x$. This constructs one candidate:

$$
F_0(x)=x^3-2x^2+5x.
$$

Check the candidate rather than assuming the reverse calculation is correct:

$$
F_0'(x)=3x^2-4x+5.
$$

Adding a constant changes the height of the graph but not its slope, so every function

$$
F(x)=x^3-2x^2+5x+C,\qquad C\in\mathbb R,
$$

has the required derivative on $\mathbb R$. This is the entire family: if $G$ is any other antiderivative, then $(G-F_0)'=0$ on $\mathbb R$. The mean value theorem implies that $G-F_0$ is constant. No initial value is given, so there is no condition selecting a particular $C$.
