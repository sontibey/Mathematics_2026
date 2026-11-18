# Exercise 14. A Matrix That Is Its Own Inverse

## Question

Assume that a square matrix $A$ satisfies

$$
A^2=I.
$$

Show that

$$
A^{-1}=A.
$$

Then give an example of a $2\times2$ matrix different from $I$ and $-I$ that satisfies this condition, and verify it by multiplication.

## Solution

The equality $A^2=I$ means both $AA=I$ and $AA=I$ in the two inverse conditions. Therefore $A$ itself is a two-sided inverse and $A^{-1}=A$.

$$
A=\begin{pmatrix}
0 & 1 \\
1 & 0 \\
\end{pmatrix},\qquad A^2=\begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}=I.
$$

This example swaps the coordinates, is different from $I$ and $-I$, and doing the swap twice restores every vector.
