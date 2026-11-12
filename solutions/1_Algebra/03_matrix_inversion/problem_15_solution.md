# Exercise 15. Two Methods for Solving the Same System

Using the inverse,

$$
A^{-1}=\frac15\begin{pmatrix}
3 & -1 \\
-1 & 2 \\
\end{pmatrix},\qquad x=\frac15\begin{pmatrix}
21-8 \\
-7+16 \\
\end{pmatrix}=\begin{pmatrix}
13/5 \\
9/5 \\
\end{pmatrix}.
$$

For elimination, apply $R_2\leftarrow R_2-\frac12R_1$ to the augmented system:

$$
\begin{pmatrix}
2 & 1 & \mid & 7 \\
0 & 5/2 & \mid & 9/2 \\
\end{pmatrix}
$$

Back substitution gives $x_2=9/5$ and $x_1=(7-9/5)/2=13/5$. Both methods agree; $2(13/5)+9/5=7$ and $13/5+3(9/5)=8$. The inverse method requires a determinant, four inverse entries, and a matrix–vector product. Elimination requires one row elimination followed by two back substitutions, so it is simpler for this single right-hand side. An already available inverse would change that comparison.
