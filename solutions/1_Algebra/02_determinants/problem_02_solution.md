# Exercise 2. Determinant of a 3×3 Matrix

Sarrus' rule subtracts the sum of the three upward diagonal products from the sum of the three downward diagonal products.

$$
\det A=\bigl(1(3)(5)+2(4)(2)+(-1)(0)(1)\bigr)-\bigl((-1)(3)(2)+2(0)(5)+1(4)(1)\bigr)=33.
$$

For a check, $R_3\leftarrow R_3-2R_1$ preserves the determinant and gives

$$
\begin{pmatrix}
1 & 2 & -1 \\
0 & 3 & 4 \\
0 & -3 & 7 \\
\end{pmatrix}
$$

Expanding along the first column gives $3(7)-4(-3)=33$, confirming the answer.
