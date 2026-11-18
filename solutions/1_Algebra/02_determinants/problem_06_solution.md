# Exercise 6. Parameter and Invertibility

## Question

For

$$
A(t)=
\begin{pmatrix}
t & 1 \\
2 & t \\
\end{pmatrix}
$$

find all values of $t$ for which the matrix is not invertible. Explain how your answer is related to the determinant being zero.

## Solution

$$
\det A(t)=t^2-2.
$$

A square matrix is not invertible exactly when its determinant vanishes. Thus $t^2=2$, so

$$
t\in\{-\sqrt2,\sqrt2\}.
$$

At either value, the second row is $t$ times the first because $t(t,1)=(2,t)$. This confirms row dependence. For all other real $t$, the determinant is nonzero and the matrix is invertible.
