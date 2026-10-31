# Exercise 7. Identity Matrix, Zero Matrix, and Powers

Here $I$ and $0$ are the $2\times2$ identity and zero matrices. The identity leaves multiplication unchanged on either side; the zero matrix leaves addition unchanged.

$$
AI=IA=A+0=\begin{pmatrix}
2 & 1 \\
0 & 2 \\
\end{pmatrix}.
$$



$$
A^2=\begin{pmatrix}
4 & 4 \\
0 & 4 \\
\end{pmatrix},\qquad A^3=A^2A=\begin{pmatrix}
8 & 12 \\
0 & 8 \\
\end{pmatrix}.
$$

Write $A=2I+N$, where $N$ has its only nonzero entry, $1$, in position $(1,2)$. Since $N^2=0$, the binomial expansion gives, for integers $n\ge1$,

$$
A^n=2^nI+n2^{n-1}N=\begin{pmatrix}
2^n & n2^{n-1} \\
0 & 2^n \\
\end{pmatrix}.
$$

This reproduces all three computed powers; $A^0=I$ separately.
