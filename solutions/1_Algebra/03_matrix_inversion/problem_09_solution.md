# Exercise 9. Matrix Equation

## Question

Given

$$
A=
\begin{pmatrix}
1 & 2 \\
0 & 1 \\
\end{pmatrix},\qquad B=
\begin{pmatrix}
3 & 1 \\
2 & 4 \\
\end{pmatrix}.
$$

Solve the equation $AX=B$ for $X$. Before calculating, decide on which side of the equation $A^{-1}$ must be used. Then check the result by computing $AX$.

## Solution

Multiply on the left: $A^{-1}AX=A^{-1}B$, so $X=A^{-1}B$. Right multiplication would not cancel $A$, because $X$ lies between the factors.

$$
X=\begin{pmatrix}
1 & -2 \\
0 & 1 \\
\end{pmatrix}\begin{pmatrix}
3 & 1 \\
2 & 4 \\
\end{pmatrix}=\begin{pmatrix}
-1 & -7 \\
2 & 4 \\
\end{pmatrix}.
$$

$$
AX=\begin{pmatrix}
-1+4 & -7+8 \\
2 & 4 \\
\end{pmatrix}=\begin{pmatrix}
3 & 1 \\
2 & 4 \\
\end{pmatrix}=B.
$$
