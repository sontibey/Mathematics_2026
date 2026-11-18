# Exercise 11. When Do Matrices Commute?

## Question

Given

$$
A=
\begin{pmatrix}
1 & 1 \\
0 & 1 \\
\end{pmatrix},\qquad B=
\begin{pmatrix}
a & b \\
c & d \\
\end{pmatrix}.
$$

Find the conditions on $a,b,c,d$ under which $AB=BA$. Describe the general form of all such matrices $B$.

## Solution

$$
AB=\begin{pmatrix}
a+c & b+d \\
c & d \\
\end{pmatrix},\qquad BA=\begin{pmatrix}
a & a+b \\
c & c+d \\
\end{pmatrix}.
$$

Equality of corresponding entries gives $c=0$ and $d=a$; there is no restriction on $b$. Hence all and only the commuting matrices are

$$
B=\begin{pmatrix}
a & b \\
0 & a \\
\end{pmatrix},\qquad a,b\in\mathbb{R}.
$$

Substituting this form into both products gives rows $(a,a+b)$ and $(0,a)$, verifying sufficiency as well as necessity.
