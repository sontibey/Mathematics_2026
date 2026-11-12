# Exercise 13. Determinant by Elimination

Apply $R_2\leftarrow R_2-2R_1$; the determinant is unchanged:

$$
\begin{pmatrix}
1 & 2 & 3 \\
0 & 1 & 1 \\
1 & 0 & 2 \\
\end{pmatrix}
$$

Apply $R_3\leftarrow R_3-R_1$; the determinant is unchanged:

$$
\begin{pmatrix}
1 & 2 & 3 \\
0 & 1 & 1 \\
0 & -2 & -1 \\
\end{pmatrix}
$$

Apply $R_3\leftarrow R_3+2R_2$; the determinant is unchanged:

$$
\begin{pmatrix}
1 & 2 & 3 \\
0 & 1 & 1 \\
0 & 0 & 1 \\
\end{pmatrix}
$$

$$
\det A=1\cdot1\cdot1=1.
$$

All three operations are row additions; there are no swaps or scalings to correct. As an independent arithmetic check, first-row expansion gives $10-2(4-7)+3(0-5)=10+6-15=1$.
