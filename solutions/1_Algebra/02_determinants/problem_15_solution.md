# Exercise 15. Combining Determinant Properties

First apply multiplicativity to the three factors, then use the inverse and transpose properties:

$$
\begin{aligned}
\det(B^{-1}A^TB)&=\det(B^{-1})\det(A^T)\det B \\
&=\frac{1}{\det B}\det A\det B \\
&=\frac13(-2)(3)=-2.
\end{aligned}
$$

The $B$ factors cancel because $\det(B^{-1})\det B=1$, valid since $B$ is invertible. This also illustrates that conjugating $A^T$ by $B$ leaves its determinant unchanged.
