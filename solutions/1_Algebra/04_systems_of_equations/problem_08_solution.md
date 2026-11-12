# Exercise 8. Two Systems with the Same Coefficient Matrix

Use $R_2\leftarrow R_2-\frac12R_1$ in each system. The two resulting augmented matrices are

$$
\begin{pmatrix}
2 & 1 & \mid & 5 \\
0 & -3/2 & \mid & -3/2 \\
\end{pmatrix},\qquad \begin{pmatrix}
2 & 1 & \mid & 1 \\
0 & -3/2 & \mid & 7/2 \\
\end{pmatrix}.
$$

The first gives $(x,y)=(2,1)$; the second gives $(x,y)=(5/3,-7/3)$. Checks: $4+1=5$, $2-1=1$, $10/3-7/3=1$, and $5/3+7/3=4$. The multiplier and transformed coefficient entries are identical because the coefficient matrix is the same; only the transformed right-hand sides differ.
