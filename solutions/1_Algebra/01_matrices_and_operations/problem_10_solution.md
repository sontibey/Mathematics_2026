# Exercise 10. Columns of a Matrix Product

## Question

Given

$$
A=
\begin{pmatrix}
1 & 2 & 0 \\
0 & 1 & 1 \\
\end{pmatrix},\qquad B=
\begin{pmatrix}
1 & 2 \\
-1 & 0 \\
3 & 1 \\
\end{pmatrix}.
$$

Denote the columns of $B$ by $b_1,b_2$.

1. Compute $Ab_1$ and $Ab_2$.
2. Compute the matrix $AB$.
3. Compare the results and explain why the columns of $AB$ are exactly the vectors $Ab_1$ and $Ab_2$.

## Solution

$$
Ab_1=\begin{pmatrix}
1-2+0 \\
0-1+3 \\
\end{pmatrix}=\begin{pmatrix}
-1 \\
2 \\
\end{pmatrix},\qquad Ab_2=\begin{pmatrix}
2+0+0 \\
0+0+1 \\
\end{pmatrix}=\begin{pmatrix}
2 \\
1 \\
\end{pmatrix}.
$$

$$
AB=\begin{pmatrix}
-1 & 2 \\
2 & 1 \\
\end{pmatrix}.
$$

The $(i,j)$ entry is the dot product of row $i$ of $A$ with column $b_j$ of $B$. Therefore column $j$ of $AB$ is $Ab_j$, which agrees with both separately computed vectors.
