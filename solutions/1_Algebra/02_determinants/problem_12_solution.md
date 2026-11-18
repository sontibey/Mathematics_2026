# Exercise 12. A Parameter Revealed by a Row Operation

## Question

For

$$
A(t)=
\begin{pmatrix}
1 & 2 & 3 \\
2 & 4 & t \\
0 & 1 & 1 \\
\end{pmatrix}
$$

find the values of $t$ for which the matrix is not invertible.

Before computing the determinant, perform the operation

$$
R_2\leftarrow R_2-2R_1
$$

and use the resulting structure. At the end, explain what special thing happens to the rows for the value of the parameter you found.

## Solution

First perform the specified operation $R_2\leftarrow R_2-2R_1$. This preserves the determinant and gives

$$
\begin{pmatrix}
1 & 2 & 3 \\
0 & 0 & t-6 \\
0 & 1 & 1 \\
\end{pmatrix}
$$

Expand along the first column; the remaining $2\times2$ determinant is

$$
\det A(t)=0\cdot1-(t-6)\cdot1=6-t.
$$

Therefore the matrix is not invertible exactly when $t=6$. At this value the transformed second row is zero; in the original matrix, $R_2=2R_1$. For $t\ne6$, the determinant is nonzero.
