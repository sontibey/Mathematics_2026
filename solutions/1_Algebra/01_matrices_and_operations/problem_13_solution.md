# Exercise 13. A Recurrence Written in Matrix Form

$$
F^2=\begin{pmatrix}
2 & 1 \\
1 & 1 \\
\end{pmatrix},\qquad F^3=\begin{pmatrix}
3 & 2 \\
2 & 1 \\
\end{pmatrix}.
$$

$$
F^4=\begin{pmatrix}
5 & 3 \\
3 & 2 \\
\end{pmatrix},\qquad F^5=\begin{pmatrix}
8 & 5 \\
5 & 3 \\
\end{pmatrix}.
$$

Let $f_0=0$, $f_1=1$, and $f_{n+1}=f_n+f_{n-1}$. The entries are consecutive Fibonacci numbers, arranged as

$$
F^n=\begin{pmatrix}
f_{n+1} & f_n \\
f_n & f_{n-1} \\
\end{pmatrix}\qquad(n\ge1).
$$

$$
F\begin{pmatrix}
a \\
b \\
\end{pmatrix}=\begin{pmatrix}
a+b \\
a \\
\end{pmatrix}.
$$

If $(a,b)=(f_{n+1},f_n)$, multiplication produces $(f_{n+2},f_{n+1})$: it forms the next sum and retains the previous first term. Multiplying the displayed general matrix by $F$ gives the same formula for $n+1$; the case $n=1$ is $F$ itself.
