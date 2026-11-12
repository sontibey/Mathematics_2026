# Exercise 7. Inverse of a Product

$$
AB=\begin{pmatrix}
2 & 3 \\
0 & 3 \\
\end{pmatrix},\qquad (AB)^{-1}=\begin{pmatrix}
1/2 & -1/2 \\
0 & 1/3 \\
\end{pmatrix}.
$$

$$
B^{-1}A^{-1}=\begin{pmatrix}
1/2 & 0 \\
0 & 1/3 \\
\end{pmatrix}\begin{pmatrix}
1 & -1 \\
0 & 1 \\
\end{pmatrix}=\begin{pmatrix}
1/2 & -1/2 \\
0 & 1/3 \\
\end{pmatrix}.
$$

The matrices agree, and $(AB)(B^{-1}A^{-1})=AIA^{-1}=I$. The product $AB$ applies $B$ first and then $A$; undo $A$ first and then $B$, giving $B^{-1}A^{-1}$.
