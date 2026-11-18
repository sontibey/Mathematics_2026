# Exercise 3. Swapping Two Rows

## Question

For

$$
A=
\begin{pmatrix}
1 & 2 & 0 \\
0 & 3 & 1 \\
2 & 1 & 1 \\
\end{pmatrix}
$$

compute $\det A$. Then form a matrix $B$ by swapping the first and second rows of $A$.

First predict $\det B$ using a determinant property, and then verify your prediction by calculation.

## Solution

Expanding along the first row,

$$
\det A=1(3\cdot1-1\cdot1)-2(0\cdot1-1\cdot2)=2+4=6.
$$

Swapping the first two rows changes the determinant sign. Therefore the prediction is $\det B=-6$, where

$$
B=\begin{pmatrix}
0 & 3 & 1 \\
1 & 2 & 0 \\
2 & 1 & 1 \\
\end{pmatrix}.
$$

Direct expansion along its first row verifies

$$
\det B=0-3(1\cdot1-0\cdot2)+1(1\cdot1-2\cdot2)=-3-3=-6.
$$
