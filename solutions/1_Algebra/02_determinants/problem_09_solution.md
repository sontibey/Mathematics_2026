# Exercise 9. Area and the Determinant

## Question

The vectors

$$
u=
\begin{pmatrix}
3 \\
1 \\
\end{pmatrix},\qquad v=
\begin{pmatrix}
1 \\
4 \\
\end{pmatrix}
$$

span a parallelogram. Compute its area using a determinant. Then reverse the order of the vectors and explain what changes in the determinant and what does not change in the area.

## Solution

Place the spanning vectors in the columns of a matrix.

$$
M=\begin{pmatrix}
3 & 1 \\
1 & 4 \\
\end{pmatrix},\qquad \det M=3(4)-1(1)=11.
$$

The parallelogram area is $|\det M|=11$ square units. Reversing the vectors swaps the columns:

$$
N=\begin{pmatrix}
1 & 3 \\
4 & 1 \\
\end{pmatrix},\qquad \det N=1(1)-3(4)=-11.
$$

The sign changes because the orientation reverses, but the absolute determinant and hence the area remain 11.
