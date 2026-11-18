# Exercise 1. Matrix Size and Entries

## Question

Given

$$
A=
\begin{pmatrix}
2 & -1 & 3 \\
0 & 4 & 5 \\
\end{pmatrix},\qquad B=
\begin{pmatrix}
1 & 0 \\
-2 & 3 \\
4 & 1 \\
\end{pmatrix}.
$$

1. State the sizes of matrices $A$ and $B$.
2. Read off the entries $a_{12}$, $a_{23}$, $b_{21}$, and $b_{32}$.
3. Write the second row of $A$ and the first column of $B$ as vectors.

## Solution

An $m\times n$ matrix has $m$ rows and $n$ columns. Thus $A$ is $2\times3$ and $B$ is $3\times2$. The first index selects the row and the second selects the column.

$$
a_{12}=-1,\qquad a_{23}=5,\qquad b_{21}=-2,\qquad b_{32}=1.
$$

The requested row and column vectors are

$$
R_2(A)=\begin{pmatrix}
0 & 4 & 5 \\
\end{pmatrix},\qquad C_1(B)=\begin{pmatrix}
1 \\
-2 \\
4 \\
\end{pmatrix}.
$$

Their lengths, three and three, agree with the number of columns of $A$ and rows of $B$, respectively.
