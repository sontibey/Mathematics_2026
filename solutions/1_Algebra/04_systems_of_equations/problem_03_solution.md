# Exercise 3. Inconsistent System

## Question

Solve or show that the system is inconsistent:

$$
\begin{cases}
x+2y=3, \\
2x+4y=7.
\end{cases}
$$

Show how the contradiction appears in the matrix after elimination and interpret it in terms of equations.

## Solution

The operation $R_2\leftarrow R_2-2R_1$ gives

$$
\begin{pmatrix}
1 & 2 & \mid & 3 \\
0 & 0 & \mid & 1 \\
\end{pmatrix}
$$

The second row asserts $0=1$, which is impossible. Therefore there is no solution. Geometrically, the left sides are proportional, but the right sides are not, so the two lines are distinct and parallel.
