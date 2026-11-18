# Exercise 9. Composing Transformations

## Question

Let

$$
S=
\begin{pmatrix}
2 & 0 \\
0 & 1 \\
\end{pmatrix},\qquad R=
\begin{pmatrix}
0 & -1 \\
1 & 0 \\
\end{pmatrix}.
$$

The matrix $S$ describes nonuniform scaling, while $R$ describes a $90^\circ$ counterclockwise rotation.
For

$$
x=
\begin{pmatrix}
1 \\
2 \\
\end{pmatrix}
$$

compute $RSx$ and $SRx$. Compare the results and explain geometrically why the order of these transformations matters.

## Solution

Apply the rightmost transformation first.

$$
Sx=\begin{pmatrix}
2 \\
2 \\
\end{pmatrix},\qquad RSx=\begin{pmatrix}
-2 \\
2 \\
\end{pmatrix}.
$$

$$
Rx=\begin{pmatrix}
-2 \\
1 \\
\end{pmatrix},\qquad SRx=\begin{pmatrix}
-4 \\
1 \\
\end{pmatrix}.
$$

Scaling first doubles the original horizontal coordinate, which becomes the vertical coordinate after rotation. Rotating first makes the original vertical coordinate horizontal, and that coordinate is then doubled. These are different directions to stretch, explaining the unequal results. As a check, $RS$ has rows $(0,-1)$ and $(2,0)$, while $SR$ has rows $(0,-2)$ and $(1,0)$.
