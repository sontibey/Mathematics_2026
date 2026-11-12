# Exercise 2. Gaussian Elimination — One Solution

From the augmented matrix, use $R_2\leftarrow R_2-2R_1$ and $R_3\leftarrow R_3-R_1$:

$$
\begin{pmatrix}
1 & 1 & 1 & \mid & 6 \\
0 & -3 & -1 & \mid & -9 \\
0 & 1 & -2 & \mid & -4 \\
\end{pmatrix}
$$

Next $R_3\leftarrow R_3+R_2/3$ gives $-7z/3=-7$, so $z=3$. Back substitution gives $-3y-3=-9$, hence $y=2$, and $x=1$. All checks hold: $1+2+3=6$, $2-2+3=3$, and $1+4-3=2$. Three pivots imply exactly one solution.
