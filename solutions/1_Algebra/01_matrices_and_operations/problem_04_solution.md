# Exercise 4. Matrix Multiplication and Noncommutativity

Each product entry is a row–column dot product.

$$
AB=\begin{pmatrix}
1(2)+2(3) & 1(0)+2(1) \\
0(2)+1(3) & 0(0)+1(1) \\
\end{pmatrix}=\begin{pmatrix}
8 & 2 \\
3 & 1 \\
\end{pmatrix}.
$$

$$
BA=\begin{pmatrix}
2(1)+0(0) & 2(2)+0(1) \\
3(1)+1(0) & 3(2)+1(1) \\
\end{pmatrix}=\begin{pmatrix}
2 & 4 \\
3 & 7 \\
\end{pmatrix}.
$$

Thus $AB\ne BA$, for example because their $(1,1)$ entries are $8$ and $2$. Matrix multiplication is noncommutative: reversing the factors can change the result.
