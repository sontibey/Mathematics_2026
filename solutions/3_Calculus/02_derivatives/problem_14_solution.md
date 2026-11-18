# Exercise 14. Continuity and Differentiability of a Piecewise Function

## Question

Investigate the behavior at $x=0$ of

$$
f(x)=
\begin{cases}
x^2,&x\ge0, \\
ax,&x<0.
\end{cases}
$$

For which values of $a$ is the function continuous? For which values do the one-sided derivatives exist and agree? For which value of $a$ is the function differentiable? Explain why continuity alone is not sufficient.

## Solution

For every real $a$, both one-sided limits at zero are zero, equal to $f(0)=0$, so the function is continuous for all $a$. From the difference quotient at zero, the right side is $h^2/h=h\to0$ and the left side is $ah/h=a$. Thus both one-sided derivatives exist for every $a$, but they agree exactly when $a=0$. The function is differentiable at zero only for $a=0$, with derivative zero. When $a\ne0$, the graph has unequal one-sided tangent slopes despite being continuous.
