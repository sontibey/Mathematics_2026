# Exercise 11. Parameter and Invertibility

## Question

For

$$
A(t)=
\begin{pmatrix}
1 & t \\
t & 1 \\
\end{pmatrix}
$$

find all $t$ for which the matrix is invertible, and then give a formula for $A(t)^{-1}$. Explain what happens to this formula at the excluded values.

## Solution

$$
\det A(t)=1-t^2.
$$

Invertibility holds exactly for $t\ne\pm1$. At these values,

$$
A(t)^{-1}=\frac1{1-t^2}\begin{pmatrix}
1 & -t \\
-t & 1 \\
\end{pmatrix}.
$$

Multiplying the numerator matrix by $A(t)$ gives $(1-t^2)I$, verifying the formula. At $t=1$ the rows coincide; at $t=-1$ they are negatives. The denominator is zero and the inverse does not exist, rather than being defined by this formula.
