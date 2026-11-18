# Exercise 7. Using Determinant Properties

## Question

Suppose that for a $3\times3$ matrix, $\det A=-4$. Compute

$$
\det(2A),\qquad \det(A^T),\qquad \det(A^2),\qquad \det(-A).
$$

Justify each answer using the appropriate property.

## Solution

For an $n\times n$ matrix, scaling the entire matrix by $c$ scales each of its $n$ rows, giving $\det(cA)=c^n\det A$. Here $n=3$.

$$
\det(2A)=2^3(-4)=-32.
$$

Transposition preserves the determinant:

$$
\det(A^T)=\det A=-4.
$$

The determinant is multiplicative:

$$
\det(A^2)=(\det A)^2=16.
$$

Scaling by $-1$ gives

$$
\det(-A)=(-1)^3(-4)=4.
$$
