# Exercise 12. Formula for a Matrix Power

## Question

Let

$$
A=
\begin{pmatrix}
1 & 1 \\
0 & 1 \\
\end{pmatrix}.
$$

Compute $A^2$, $A^3$, and $A^4$, and use them to formulate a conjecture for $A^n$. Then do not stop after checking one more case: assume the formula is true for $n$, multiply by $A$, and explain why you obtain exactly the formula for $n+1$.

## Solution

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
