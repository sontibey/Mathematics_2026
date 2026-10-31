# Exercise 12. Formula for a Matrix Power

$$
A^2=\begin{pmatrix}
1 & 2 \\
0 & 1 \\
\end{pmatrix},\qquad A^3=\begin{pmatrix}
1 & 3 \\
0 & 1 \\
\end{pmatrix},\qquad A^4=\begin{pmatrix}
1 & 4 \\
0 & 1 \\
\end{pmatrix}.
$$

The conjecture is $A^n$ with rows $(1,n)$ and $(0,1)$ for every integer $n\ge0$. For the base case $n=0$, the formula gives $I=A^0$. Assume the formula holds for $n$. Then

$$
A^{n+1}=A^nA=\begin{pmatrix}
1 & n \\
0 & 1 \\
\end{pmatrix}\begin{pmatrix}
1 & 1 \\
0 & 1 \\
\end{pmatrix}=\begin{pmatrix}
1 & n+1 \\
0 & 1 \\
\end{pmatrix}.
$$

The product has exactly the asserted form with $n+1$ in place of $n$. Mathematical induction proves the formula for every nonnegative integer.
