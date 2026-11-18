# Exercise 13. Undoing a Composite Transformation

## Question

The matrices

$$
S=
\begin{pmatrix}
2 & 0 \\
0 & 1 \\
\end{pmatrix},\qquad H=
\begin{pmatrix}
1 & 1 \\
0 & 1 \\
\end{pmatrix}
$$

describe nonuniform scaling and shear. For $T=HS$, find $T^{-1}$ in two ways:

1. first compute $T$, then its inverse,
2. use $(HS)^{-1}=S^{-1}H^{-1}$.

Compare the results. Additionally compute $H^{-1}S^{-1}$ and verify that the incorrect order gives a different matrix. Explain the rule: “when undoing a composition of operations, we undo them from the end.”

## Solution

$$
T=HS=\begin{pmatrix}
2 & 1 \\
0 & 1 \\
\end{pmatrix},\qquad T^{-1}=\begin{pmatrix}
1/2 & -1/2 \\
0 & 1 \\
\end{pmatrix}.
$$

The second method gives

$$
S^{-1}H^{-1}=\begin{pmatrix}
1/2 & 0 \\
0 & 1 \\
\end{pmatrix}\begin{pmatrix}
1 & -1 \\
0 & 1 \\
\end{pmatrix}=\begin{pmatrix}
1/2 & -1/2 \\
0 & 1 \\
\end{pmatrix}.
$$

In the other order,

$$
H^{-1}S^{-1}=\begin{pmatrix}
1/2 & -1 \\
0 & 1 \\
\end{pmatrix}.
$$

This differs in its $(1,2)$ entry, and multiplying it on the left by $T$ gives rows $(1,-1)$ and $(0,1)$, not $I$. Since $T$ scales and then shears, its inverse must undo the shear and then the scaling. The correct product satisfies $TT^{-1}=I$.
