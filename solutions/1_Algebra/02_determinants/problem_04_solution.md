# Exercise 4. Triangular Matrix

## Question

Without expanding the determinant, compute

$$
\det
\begin{pmatrix}
2 & 4 & 1 \\
0 & -3 & 5 \\
0 & 0 & 7 \\
\end{pmatrix}.
$$

State the rule for an arbitrary triangular matrix and explain it using this example.

## Solution

The determinant of any square upper or lower triangular matrix is the product of its diagonal entries. Here,

$$
\det A=2(-3)(7)=-42.
$$

The zeros below the diagonal force every nonzero term in the determinant permutation formula to use the diagonal entries. The entries above the diagonal do not affect this product.
