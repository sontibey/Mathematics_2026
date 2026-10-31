# Exercise 9. Composing Transformations

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
