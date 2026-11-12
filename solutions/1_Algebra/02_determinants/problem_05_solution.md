# Exercise 5. Row Operations

Each operation below adds a multiple of another row, so each preserves the determinant. First use $R_2\leftarrow R_2-2R_1$:

$$
\begin{pmatrix}
1 & 2 & 3 \\
0 & -3 & -6 \\
-1 & 4 & 2 \\
\end{pmatrix}
$$

Then use $R_3\leftarrow R_3+R_1$:

$$
\begin{pmatrix}
1 & 2 & 3 \\
0 & -3 & -6 \\
0 & 6 & 5 \\
\end{pmatrix}
$$

Finally use $R_3\leftarrow R_3+2R_2$:

$$
\begin{pmatrix}
1 & 2 & 3 \\
0 & -3 & -6 \\
0 & 0 & -7 \\
\end{pmatrix}
$$

$$
\det A=1(-3)(-7)=21.
$$

No swaps or row scalings occurred, so no correction factor is needed. Checking by first-row expansion gives $2-8+27=21$.
