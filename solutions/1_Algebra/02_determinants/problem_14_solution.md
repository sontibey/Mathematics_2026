# Exercise 14. A System of Equations and the Determinant

## Question

Consider the system $Ax=b$, where

$$
A=
\begin{pmatrix}
1 & 2 \\
k & 4 \\
\end{pmatrix}.
$$

For which values of $k$ does the system have exactly one solution for every $b$? For the remaining value, give an example of a right-hand side $b$ for which the system has infinitely many solutions, and an example for which it has no solution.

## Solution

$$
\det A=4-2k.
$$

Exactly one solution exists for every $b\in\mathbb{R}^2$ if and only if $A$ is invertible, so the answer is $k\ne2$.

At $k=2$, the second left-hand side is twice the first. Consistency therefore requires $b_2=2b_1$. For example, choose

$$
b=\begin{pmatrix}
1 \\
2 \\
\end{pmatrix}.
$$

Then the equations reduce to $x_1+2x_2=1$, with infinitely many solutions

$$
x=\begin{pmatrix}
1-2s \\
s \\
\end{pmatrix},\qquad s\in\mathbb{R}.
$$

Substitution gives $Ax=(1,2)^T$ for every $s$. In contrast, choose

$$
b=\begin{pmatrix}
1 \\
3 \\
\end{pmatrix}.
$$

The first equation would force the second left-hand side to equal 2, whereas the second equation requires 3. Thus there is no solution.
