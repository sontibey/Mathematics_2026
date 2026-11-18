# Exercise 1. Definition of the Inverse

## Question

For

$$
A=
\begin{pmatrix}
2 & 1 \\
1 & 1 \\
\end{pmatrix},\qquad B=
\begin{pmatrix}
1 & -1 \\
-1 & 2 \\
\end{pmatrix}
$$

check, without using a formula, whether $B=A^{-1}$. Compute $AB$ and $BA$ and relate the result to the definition of the inverse.

## Solution

Multiplying in both orders gives

$$
AB=\begin{pmatrix}
2-1 & -2+2 \\
1-1 & -1+2 \\
\end{pmatrix}=I,\qquad BA=\begin{pmatrix}
2-1 & 1-1 \\
-2+2 & -1+2 \\
\end{pmatrix}=I.
$$

The definition of $A^{-1}$ is a matrix whose products with $A$, on either side, equal $I$. Thus $B=A^{-1}$.
