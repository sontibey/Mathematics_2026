# Exercise 6. Transpose

Transposing interchanges rows and columns.

$$
A^T=\begin{pmatrix}
1 & 4 \\
2 & 5 \\
3 & 6 \\
\end{pmatrix},\qquad B^T=\begin{pmatrix}
1 & 2 & -1 \\
0 & 1 & 3 \\
\end{pmatrix}.
$$

$$
AB=\begin{pmatrix}
1+4-3 & 0+2+9 \\
4+10-6 & 0+5+18 \\
\end{pmatrix}=\begin{pmatrix}
2 & 11 \\
8 & 23 \\
\end{pmatrix}.
$$

$$
(AB)^T=\begin{pmatrix}
2 & 8 \\
11 & 23 \\
\end{pmatrix}=B^TA^T.
$$

Indeed the rows of $B^T$ dotted with the columns of $A^T$ give $(2,8)$ and $(11,23)$. The factor order reverses under transposition.
