# Exercise 5. Matrix Times Vector

## Question

Let

$$
A=
\begin{pmatrix}
2 & -1 \\
1 & 3 \\
\end{pmatrix},\qquad x=
\begin{pmatrix}
4 \\
2 \\
\end{pmatrix}.
$$

Compute $Ax$. Then express $Ax$ as a linear combination of the columns of $A$, with coefficients coming from the vector $x$.

## Solution

$$
Ax=\begin{pmatrix}
2(4)-1(2) \\
1(4)+3(2) \\
\end{pmatrix}=\begin{pmatrix}
6 \\
10 \\
\end{pmatrix}.
$$

The vector entries weight the corresponding columns of $A$:

$$
Ax=4\begin{pmatrix}
2 \\
1 \\
\end{pmatrix}+2\begin{pmatrix}
-1 \\
3 \\
\end{pmatrix}=\begin{pmatrix}
8 \\
4 \\
\end{pmatrix}+\begin{pmatrix}
-2 \\
6 \\
\end{pmatrix}=\begin{pmatrix}
6 \\
10 \\
\end{pmatrix}.
$$

The column combination agrees with the row–column calculation.
