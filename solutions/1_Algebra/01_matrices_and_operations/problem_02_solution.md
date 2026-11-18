# Exercise 2. Addition and Scalar Multiplication

## Question

For

$$
A=
\begin{pmatrix}
1 & 2 \\
-1 & 3 \\
\end{pmatrix},\qquad B=
\begin{pmatrix}
4 & -2 \\
0 & 5 \\
\end{pmatrix}
$$

compute

$$
A+B,\qquad A-B,\qquad 3A-2B.
$$

Explain why matrix addition is possible only for matrices of the same size.

## Solution

Add or subtract corresponding entries, and multiply every entry by the scalar.

$$
A+B=\begin{pmatrix}
5 & 0 \\
-1 & 8 \\
\end{pmatrix},\qquad A-B=\begin{pmatrix}
-3 & 4 \\
-1 & -2 \\
\end{pmatrix}.
$$

$$
3A-2B=\begin{pmatrix}
3 & 6 \\
-3 & 9 \\
\end{pmatrix}-\begin{pmatrix}
8 & -4 \\
0 & 10 \\
\end{pmatrix}=\begin{pmatrix}
-5 & 10 \\
-3 & -1 \\
\end{pmatrix}.
$$

Addition requires equal sizes so that every entry has a corresponding entry in the other matrix. As a check, subtracting $B$ from the computed $A+B$ recovers $A$; also $(3A-2B)+2B=3A$.
