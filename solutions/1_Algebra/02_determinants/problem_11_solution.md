# Exercise 11. Shortening the Calculation with Row Operations

Use $R_2\leftarrow R_2-R_1$, which preserves the determinant:

$$
\begin{pmatrix}
1 & 2 & 3 \\
0 & 1 & 1 \\
1 & 4 & 6 \\
\end{pmatrix}
$$

Use $R_3\leftarrow R_3-R_1$, again preserving it:

$$
\begin{pmatrix}
1 & 2 & 3 \\
0 & 1 & 1 \\
0 & 2 & 3 \\
\end{pmatrix}
$$

Use $R_3\leftarrow R_3-2R_2$, also preserving it:

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

In general, adding any multiple of one row to a different row leaves the determinant unchanged. The triangular result needs no sign or scaling correction.
