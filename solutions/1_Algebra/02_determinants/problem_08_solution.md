# Exercise 8. Determinant of a Product

## Question

Let $A,B$ be square matrices such that $\det A=3$ and $\det B=-5$. Compute $\det(AB)$, $\det(BA)$ and, if it exists, $\det(A^{-1}B)$. Explain why the first two results are equal even though usually $AB\neq BA$.

## Solution

Assume $A$ and $B$ have the same square size, as required by the products. Multiplicativity gives

$$
\det(AB)=3(-5)=-15,\qquad \det(BA)=(-5)3=-15.
$$

Since $\det A=3\ne0$, the inverse exists and $\det(A^{-1})=1/3$. Consequently,

$$
\det(A^{-1}B)=\frac13(-5)=-\frac53.
$$

The first two determinants agree because scalar multiplication commutes. Equality of determinants does not imply equality of matrices, so this does not require $AB=BA$.
