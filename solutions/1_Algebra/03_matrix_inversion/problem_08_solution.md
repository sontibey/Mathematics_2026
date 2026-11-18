# Exercise 8. Inverse of a Transformation

## Question

The matrix

$$
S=
\begin{pmatrix}
2 & 0 \\
0 & \frac12 \\
\end{pmatrix}
$$

describes a scaling of the plane. Find $S^{-1}$ and explain geometrically what the inverse transformation does. Check the action of the pair $S,S^{-1}$ on one simple vector.

## Solution

$$
S^{-1}=\begin{pmatrix}
1/2 & 0 \\
0 & 2 \\
\end{pmatrix}.
$$

It halves horizontal coordinates and doubles vertical coordinates, reversing the original scaling. For example, $(2,4)$ is sent by $S$ to $(4,2)$ and by $S^{-1}$ back to $(2,4)$. Both products $SS^{-1}$ and $S^{-1}S$ have diagonal entries 1 and zero off-diagonal entries, so they equal $I$.
