# Exercise 8. Row Operations and Their Reversibility

After $R_2\leftarrow R_2-2R_1$:

$$
\begin{pmatrix}
1 & 2 & -1 \\
0 & 0 & 3 \\
-1 & 1 & 3 \\
\end{pmatrix}
$$

After $R_3\leftarrow R_3+R_1$:

$$
\begin{pmatrix}
1 & 2 & -1 \\
0 & 0 & 3 \\
0 & 3 & 2 \\
\end{pmatrix}
$$

After $R_2\leftrightarrow R_3$:

$$
\begin{pmatrix}
1 & 2 & -1 \\
0 & 3 & 2 \\
0 & 0 & 3 \\
\end{pmatrix}
$$

The inverse of the first operation is $R_2\leftarrow R_2+2R_1$; the inverse of the second is $R_3\leftarrow R_3-R_1$; a row swap is its own inverse. To recover the original matrix, undo the swap first, then subtract $R_1$ from $R_3$, then add $2R_1$ to $R_2$. These restore the original rows exactly.
