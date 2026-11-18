# Exercise 10. Inverse of a Diagonal Matrix

## Question

Given

$$
D=
\begin{pmatrix}
2 & 0 & 0 \\
0 & -3 & 0 \\
0 & 0 & 5 \\
\end{pmatrix},\qquad E=
\begin{pmatrix}
2 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 5 \\
\end{pmatrix}.
$$

Without using Gauss–Jordan elimination, decide which matrix is invertible. For the invertible matrix, give the inverse and check the result by multiplication.

## Solution

A diagonal matrix is invertible exactly when all its diagonal entries are nonzero. Thus $D$ is invertible, while $E$ is not: $E(0,1,0)^T=0$.

$$
D^{-1}=\begin{pmatrix}
1/2 & 0 & 0 \\
0 & -1/3 & 0 \\
0 & 0 & 1/5 \\
\end{pmatrix}.
$$

The diagonal entries in $DD^{-1}=D^{-1}D$ are $2(1/2)$, $(-3)(-1/3)$ and $5(1/5)$, all 1; every off-diagonal entry is zero. Both products equal $I_3$.
