# Exercise 12. Finding Inverses Without Starting from Scratch

Write $M=A^{-1}$. Scaling, transposition, and the product rule for inverses give

$$
(3A)^{-1}=\frac13M=\frac13\begin{pmatrix}
2 & -1 \\
-3 & 2 \\
\end{pmatrix}.
$$

$$
(A^T)^{-1}=M^T=\begin{pmatrix}
2 & -3 \\
-1 & 2 \\
\end{pmatrix}.
$$

$$
(A^2)^{-1}=M^2=\begin{pmatrix}
7 & -4 \\
-12 & 7 \\
\end{pmatrix}.
$$

For example, $(3A)(M/3)=AM=I$; $A^TM^T=(MA)^T=I$; and $A^2M^2=A(AM)M=I$. These verify the three properties without finding $A$.
