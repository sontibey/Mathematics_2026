# Exercise 4. Gauss–Jordan

Start with the augmented matrix

$$
\begin{pmatrix}
1 & 2 & \mid & 1 & 0 \\
3 & 5 & \mid & 0 & 1 \\
\end{pmatrix}
$$

Apply $R_2\leftarrow R_2-3R_1$:

$$
\begin{pmatrix}
1 & 2 & \mid & 1 & 0 \\
0 & -1 & \mid & -3 & 1 \\
\end{pmatrix}
$$

Apply $R_2\leftarrow -R_2$:

$$
\begin{pmatrix}
1 & 2 & \mid & 1 & 0 \\
0 & 1 & \mid & 3 & -1 \\
\end{pmatrix}
$$

Apply $R_1\leftarrow R_1-2R_2$:

$$
\begin{pmatrix}
1 & 0 & \mid & -5 & 2 \\
0 & 1 & \mid & 3 & -1 \\
\end{pmatrix}
$$

$$
A^{-1}=\begin{pmatrix}
-5 & 2 \\
3 & -1 \\
\end{pmatrix}.
$$

If the combined row operations represent multiplication by $E$, the left side is $EA=I$ and the right side is $EI=E$. Thus $E=A^{-1}$. Checking the result gives $AA^{-1}=I$.
